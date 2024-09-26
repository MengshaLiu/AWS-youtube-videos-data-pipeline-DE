# AWS-youtube-videos-data-pipeline-DE

## Table of Contents
- [Introduction](#introduction)
- [Architecture](#architecture)
- [Technologies Used](#technologies-used)
- [Data Source](#data-source)
- [Highlighted Features](#highlighted-features)
- [Results](#results)
- [How to Run](#how-to-run)
- [Contact](#contact)

## Introduction
The objective of this project is to develop an automated data pipeline to process trending YouTube video data for the Australian market using AWS cloud-based tools. The pipeline begins with a scraper application that extracts data from the YouTube API, followed by AWS Glue, which builds a serverless ELT workflow to transform the data and prepare it for analysis. The curated data is then analyzed and visualized using Amazon Quicksight. 

## Architecture
![project architecture](architecture.jpeg)

This project consists of several critical components:
- **Data Source**: Utilizes the YouTube API to retrieve trending video data.
- **AWS Lambda**: Executes the scraper application daily to automatically extract data from the YouTube API.
- **Amazon S3**: Acts as a data lake for storing raw, transformed, and curated datasets separately.
- **Crawler** automatically infers schema information of the data and integrates it into AWS Glue Data Catalog
- **AWS Glue**: Facilitates a serverless ELT workflow for data transformation and loading into the target database.
- **Amazon Athena (optional)**: Enabling efficient querying and analysis of data stored in S3.
- **Amazon Quicksight**: Used for visualization and generating reports.


