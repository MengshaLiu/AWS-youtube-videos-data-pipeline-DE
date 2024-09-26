import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue import DynamicFrame


def sparkSqlQuery(glueContext, query, mapping, transformation_ctx) -> DynamicFrame:
    for alias, frame in mapping.items():
        frame.toDF().createOrReplaceTempView(alias)
    result = spark.sql(query)
    return DynamicFrame.fromDF(result, glueContext, transformation_ctx)


args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node Data Catalog
DataCatalog_node1 = glueContext.create_dynamic_frame.from_catalog(
    database="youtube_trending_videos",
    table_name="au_youtube_trending_videos",
    transformation_ctx="DataCatalog_node1",
)

# Script generated for node Change Schema
ChangeSchema_node1695958535104 = ApplyMapping.apply(
    frame=DataCatalog_node1,
    mappings=[
        ("video_id", "string", "video_id", "string"),
        ("title", "string", "title", "string"),
        ("publishedat", "string", "publishedat", "timestamp"),
        ("channelid", "string", "channelid", "string"),
        ("channeltitle", "string", "channeltitle", "string"),
        ("categoryid", "string", "categoryid", "int"),
        ("trending_date", "string", "trending_date", "string"),
        ("tags", "string", "tags", "string"),
        ("view_count", "string", "view_count", "long"),
        ("likes", "string", "likes", "long"),
        ("dislikes", "string", "dislikes", "long"),
        ("comment_count", "string", "comment_count", "long"),
        ("thumbnail_link", "string", "thumbnail_link", "string"),
        ("comments_disabled", "string", "comments_disabled", "boolean"),
        ("ratings_disabled", "string", "ratings_disabled", "boolean"),
        ("description", "string", "description", "string"),
    ],
    transformation_ctx="ChangeSchema_node1695958535104",
)

# Script generated for node SQL Query
SqlQuery338 = """
select video_id,title, publishedat, channelid, channeltitle, categoryid, to_date(concat('20',trending_date), 'yyyy.dd.MM') as trending_date,tags, view_count,likes,dislikes,comment_count, thumbnail_link, comments_disabled, ratings_disabled,description 
from myDataSource
"""
SQLQuery_node1698202604944 = sparkSqlQuery(
    glueContext,
    query=SqlQuery338,
    mapping={"myDataSource": ChangeSchema_node1695958535104},
    transformation_ctx="SQLQuery_node1698202604944",
)

# Script generated for node Amazon S3
AmazonS3_node1695877434072 = glueContext.write_dynamic_frame.from_options(
    frame=SQLQuery_node1698202604944,
    connection_type="s3",
    format="csv",
    connection_options={
        "path": "s3://youtube-trending-vidoe-project/transformed/AU_Youtube_trending_videos/",
        "partitionKeys": ["trending_date"],
    },
    transformation_ctx="AmazonS3_node1695877434072",
)

job.commit()
