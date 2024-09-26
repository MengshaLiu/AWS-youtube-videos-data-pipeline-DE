import requests
import sys
import time
import boto3
import pandas as pd
import awswrangler as wr

country_code = 'AU' 
snippet_features = ["title",
                    "publishedAt",
                    "channelId",
                    "channelTitle",
                    "categoryId"]
header = ["video_id"] + snippet_features + ["trending_date", "tags","view_count", "likes", "dislikes",
                                            "comment_count", "thumbnail_link", "comments_disabled",
                                            "ratings_disabled", "description"]

def api_request(country_code, api_key, next_page_token):
    # Builds the URL and requests the JSON from it
    request_url = f"https://www.googleapis.com/youtube/v3/videos?part=id,statistics,snippet{next_page_token}chart=mostPopular&regionCode={country_code}&maxResults=50&key={api_key}"
    request = requests.get(request_url)
    if request.status_code == 429:
        print("Temp-Banned due to excess requests, please wait and continue later")
        sys.exit()
      
    return request.json()

unsafe_characters = ['\n', '"']
def prepare_feature(feature):
    # Removes any character from the unsafe characters list and surrounds the whole item in quotes
    for ch in unsafe_characters:
        feature = str(feature).replace(ch, "")
      
    return f'{feature}'

def get_videos(items):
    snippet_features = ["title",
                    "publishedAt",
                    "channelId",
                    "channelTitle",
                    "categoryId"]

    lines = []
  
    for video in items:
        comments_disabled = False
        ratings_disabled = False

        # We can assume something is wrong with the video if it has no statistics, often this means it has been deleted
        # so we can just skip it
        if "statistics" not in video:
            continue

        # A full explanation of all of these features can be found on the GitHub page for this project
        video_id = prepare_feature(video['id'])

        # Snippet and statistics are sub-dicts of video, containing the most useful info
        snippet = video['snippet']
        statistics = video['statistics']

        # This list contains all of the features in snippet that are 1 deep and require no special processing
        features = [prepare_feature(snippet.get(feature, "")) for feature in snippet_features]

        # The following are special case features which require unique processing, or are not within the snippet dict
        description = snippet.get("description", "")
        thumbnail_link = snippet.get("thumbnails", dict()).get("default", dict()).get("url", "")
        trending_date = time.strftime("%y.%d.%m")
        tags_list = snippet.get("tags", ["[none]"])
        tags = prepare_feature("|".join(tags_list))
        view_count = statistics.get("viewCount", 0)

        # This may be unclear, essentially the way the API works is that if a video has comments or ratings disabled
        # then it has no feature for it, thus if they don't exist in the statistics dict we know they are disabled
        if 'likeCount' in statistics:
            likes = statistics['likeCount']
        else:
            ratings_disabled = True
            likes = 0
        if 'commentCount' in statistics:
            comment_count = statistics['commentCount']
        else:
            comments_disabled = True
            comment_count = 0
        dislikes = 0
        # Compiles all of the various bits of info into one consistently formatted line
        line = [video_id] + features + [prepare_feature(x) for x in [trending_date, tags, view_count, likes, dislikes, 
                                                                     comment_count, thumbnail_link, comments_disabled,
                                                                       ratings_disabled, description]]
        lines.append(line)
      
    return lines

def write_to_file(video_data_df,country_code):
    wr.s3.to_parquet(df=video_data_df, path=f"s3://youtube-trending-vidoe-project/landing/{country_code}_Youtube_trending_videos/{time.strftime('%y.%d.%m')}_{country_code}_videos.parquet")
    print(f"successfully upload {country_code}_Youtube_trending_videos/{time.strftime('%y.%d.%m')}_{country_code}_videos to s3")
  
def lambda_handler(event,context):
    next_page_token = '&'
    video_df = pd.DataFrame(columns=header)
    
  while next_page_token is not None:
        video_data_page = api_request(country_code, 'AIzaSyAEXSs2Ngr8pkzgaD27Seab_VUtZHKeLU8',next_page_token)
        items = video_data_page['items']
        page_data = get_videos(items)
        page_video_df = pd.DataFrame(data = page_data, columns=header)
        video_df = pd.concat([video_df,page_video_df], ignore_index=True)
        next_page_token = video_data_page.get("nextPageToken", None)
        next_page_token = f"&pageToken={next_page_token}&" if next_page_token is not None else next_page_token
    print(video_df.dtypes)
    video_df.to_csv('video_data_page.csv')

lambda_handler('event','context')
