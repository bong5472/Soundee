from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser

DEVELOPER_KEY='자기 api 넣기'
YOUTUBE_API_SERVICE_NAME='youtube'
YOUTUBE_API_VERSION='v3'

youtube=build(YOUTUBE_API_SERVICE_NAME,YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)

search_response=youtube.search().list(
    q="검색 값",
    order='relevance',
    part='snippet',
    maxResults=50,
    ).execute()