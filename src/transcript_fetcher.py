from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
import os

class TranscriptFetcher:

    def fetch_transcript(self, video_id):
        try:
            transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
            # unique languages available
            languages = list(set(transcript.language_code for transcript in transcript_list))
            print("languages:", ", ".join(languages))
            # title = self.fetch_video_title(self, video_id)

            transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=languages)
            transcript_text = " ".join([entry["text"] for entry in transcript])
            print("\nTranscript:\n", transcript_text)

            os.makedirs(f"./cached/{video_id}", exist_ok=True)
            open(f"./cached/{video_id}/transcript.txt", "w").write(transcript_text)
            
            return transcript_text

        except TranscriptsDisabled:
            print("Transcripts are unavailable for this video.")
            # TODO: generate transcription from audio with Whisper
            # return self.generate_transcription(video_id) if isinstance(e, (TranscriptsDisabled, NoTranscriptFound)) else None
        except Exception as e:
            print(f"An error occurred: {e}")
        return None
    
    # import requests
    # from bs4 import BeautifulSoup

    # def fetch_video_title(self, video_id):
    #     """
    #     Scrapes the YouTube video page to extract the video title, or Youtube API keys.
    #     """
    #     try:
    #         url = f"https://www.youtube.com/watch?v={video_id}"
    #         response = requests.get(url)
    #         response.raise_for_status()
    #         soup = BeautifulSoup(response.text, 'html.parser')
    #         title = soup.find("title").text.replace(" - YouTube", "").strip()
    #         return title
    #     except Exception as e:
    #         print(f"Failed to fetch video title: {e}")
    #         return "Unknown Title"