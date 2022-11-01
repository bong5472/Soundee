from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser


DEVELOPER_KEY = "YOUR_CLIENT_ID"
YOUTUBE_API_SERVICE_NAME="youtube"
YOUTUBE_API_VERSION="v3"
youtube = build(YOUTUBE_API_SERVICE_NAME,YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)

search_response = youtube.search().list(
    q = "pure playlist",
    
    order = "title",
    part = "snippet",
    maxResults = 1
    ).execute()

print(search_response)


