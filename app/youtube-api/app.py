import os
from dotenv import load_dotenv
from googleapiclient.discovery import build
import pprint


console = pprint.PrettyPrinter(indent=1).pprint
load_dotenv()

api_key = os.getenv("YOUTUBE_DATA_API_KEY")
print(api_key)

youtube = build('youtube', 'v3', developerKey=api_key)

channel_details = youtube.channels().list(
  part="contentDetails, statistics",
  forUsername='schafer5'
)

playlist_details = youtube.playlists().list(
  part='contentDetails, snippet',
  channelId='UCCezIgC97PvUuR4_gbFUs5g'
)

res = playlist_details.execute()

for item in res['items']:
  console(item)