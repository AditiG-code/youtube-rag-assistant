#loading transcipt of any yt video 
from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_id):

    ytt_api = YouTubeTranscriptApi()

    transcript_list = ytt_api.fetch(
        video_id,
        #write whatever language you want ->default set english -en
        languages=["en"]
    )
    # convert transcript to plain text
    text = " ".join(
        chunk.text for chunk in transcript_list
    )

    return text