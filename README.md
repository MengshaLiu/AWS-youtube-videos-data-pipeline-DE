# AWS-youtube-videos-data-pipeline-DE

## Table of Contents
- [Introduction](#introduction)
- [Architecture](#architecture)
- [Data Source](#data-source)
- [Highlighted Features](#highlighted-features)
- [Results](#results)
- [Further Developing Opportunities](#further-developing-opportunities)
- [Contact](#contact)

## Introduction
The objective of this project is to develop an automated data pipeline to process trending YouTube video data for the Australian market using AWS cloud-based tools. The pipeline begins with a scraper application that extracts data from the YouTube API, followed by AWS Glue, which builds a serverless ELT workflow to transform the data and prepare it for analysis. The curated data is then analyzed and visualized using Amazon Quicksight. 

## Architecture
![project architecture](architecture.jpeg)

This project consists of several critical components:
- **Data Source**: retrieve a list of the most popular videos for the day based on a specified country code. The API provides metadata such as video titles, view counts, likes, comments, and categories, allowing for detailed analysis of trending content.
- **AWS Lambda**: Served as a scraper application to automatically extract data from the YouTube API on a scheduled basis.
- **AWS EventBridge**  Used to schedule and trigger the Lambda function on a daily basis, eliminating the need for manual intervention.
- **Amazon S3**: Acts as a data lake for storing raw, transformed, and curated datasets separately.
- **Crawler** automatically infers schema information of the data and integrates it into the AWS Glue Data Catalog.
- **AWS DateBrew** Used to conduct data profiling and data quality checks.
- **AWS Glue**: Facilitates a serverless ELT workflow for data transformation and loading into the target database.
- **Amazon Athena (optional)**: Enables efficient querying and analysis of data stored in S3.
- **Amazon Quicksight**: Used for visualization and generating reports.

## Data Source
- **Youtube Data API**: enables developers to interact programmatically with YouTube data. Common use cases include fetching video details, accessing trending content, searching for specific channels, and analyzing user interactions. In this project, [videos.list](https://developers.google.com/youtube/v3/docs/videos/list) function is used to retrieve detailed information about a list of daily trending videos.

## Highlighted Feature
- **Cloud-based ELT**
- **Consistent and High-Quality Data** Utilize Databrew's data profiling and quality check functions to ensure data consistency.
- **managed Data Schema** 
- **Automated ELT Pipeline** Developed an ELT pipeline that automatically ingested, loaded, and transformed data from YouTube Data API to the target cloud data storage.
- **flawless workflow management** 
## Results
### Sample Output ([Check the `output/` folder for the full sample data](data/))
This sample output contains data based on YouTube's top 200 trending videos in the AU market collected daily throughout November 2023. 
![sample output](output/sample-data-screenshot.png)
### Visualization (using sample data)
The visualisations below provide a comprehensive analysis of YouTube trending videos, emphasizing video categories during November 2023. The findings are presented through three dashboards, each focusing on distinct aspects: daily performance, engagement metrics, and video duration of various trending video categories.
#### Dashboard 1: Analysis of Daily Performance by Video Categories (November 2023)

<p align="center">
<img src="visualisation/Dashboards-01.jpeg" alt="drawing" width="700" align="top"/>
</p>

- The stacked area chart shows the number of trending videos in each category daily for November 2023. Categories like Gaming, Entertainment, and Sports consistently dominate the daily trends, while categories such as Education, Science & Technology, and Film & Animation have lower numbers but show relatively stable trends over the month.
- The stacked bar chart displays the average daily view counts for each category. Categories like Music and Entertainment show high view counts, suggesting these categories have strong daily audience exposure and attract the most attention.
<br>

#### Dashboard 2: Engagement Metrics by Video Category (November 2023)
<p align="center">
<img src="visualisation/Dashboards-02.jpeg" alt="drawing" width="700" align="top"/>
</p>

- The blue bar chart shows average video view counts per category. Music and Entertainment lead with the highest average views (approaching 9-10 million), followed by Science & Technology (around 4.56 million) and Film & Animation (around 3.6 million). Autos & Vehicles and Travel & Events have the lowest views (under 1 million).
- The green bar chart shows the average video likes per category. Music and Entertainment are the top categories for likes-clicking, closely followed by Film & Animation. Lower engagement in terms of likes is seen in categories such as Sports and News & Politics.
- The orange bar chart shows the average video comments per category. Music has the highest number of average comments which is far more than other categories, indicating strong video engagement. Entertainment and Film & Animation also receive high comment counts. Categories like News & Politics and Autos & Vehicles have fewer comments, indicating lower interaction.
- Based on the three engagement metrics, music, entertainment, and film & animation are the top 3 categories showing strong user engagement and interactions.
<br>

#### Dashboards 3: Analysis of Trending Duration (November 2023)
<p align="center">
<img src="visualisation/Dashboards-03.jpeg" alt="drawing" width="700" align="top"/>
</p>

- The pie chart shows that most videos (54.83%) remain on the trending list for 6-10 days, followed by 2-5 days (35.62%). Only a small percentage of videos trend for more than 10 days (2.32%) or 1 day (10.52%). This suggests that the typical lifespan of a trending video is under 10 days, with the majority trending for a week.
- The text table highlights average engagement metrics (views, likes, and comments) for each trending duration. Videos trending for more than 10 days attract the highest engagement, with over 16 million views, indicating that longer-trending videos gain significantly more exposure. Shorter-trending videos (1 day and 2-5 days) have lower average views and interaction.
- The bar chart breaks down video counts by category and trending duration. The Gaming and Entertainment categories dominate in trending counts, with a large portion trending for 6-10 days.
Other categories such as Sports, Music, and People & Blogs also trend frequently but with shorter durations.
Categories like Pets & Animals and Travel & Events have fewer trending durations, primarily trending for just 1-2 days, reflecting lower audience reach and engagement.

## Further Developing Opportunities
1. **Trend Analysis**
- Track the performance of various video categories over time to spot emerging trends. Understand seasonal or event-based spikes in certain content categories, like Sports during major events.
2. **Metadata Optimization**
- Analyze the titles, descriptions, and tags used by trending videos and identify high-performing keywords and tag strategies for better searching visibility. 
3. **Audience Sentiment and Engagement**
- Analyze comments and engagement metrics to access viewer sentiment of YouTube videos. Determine the sentiment distribution (positive, neutral, negative) to understand public opinion on the videos to help improve the video content in the future.
4. **Competitive Analysis for Influencers**
- Monitor competitors' channels that consistently trend and analyze the types of content they publish. Benchmark against competitors by identifying key factors—such as video categories, tags, length, titles, and publish time that contribute to their success.
5. Advertising 
Purpose: Identify the best-performing video categories and trending themes for placing targeted ads.
	•	Insights: Choose the most suitable categories and creators to maximize ad effectiveness based on audience preferences.

## Contact
For any questions or collaborations, feel free to reach out via:
- LinkedIn(https://linkedin.com/in/melissa-liu-b31892180)
- GitHub (https://github.com/MengshaLiu)
