from transcript_fetcher import TranscriptFetcher
from summarizer import Summarizer
import sys
import time

class Sumaria:

    def run(self, video_id):
        print("Fetching transcript for video", video_id)
        transcript = TranscriptFetcher().fetch_transcript(video_id)
        if transcript:
            print("\nGenerating summary...")
            summary = Summarizer().summarize(transcript, video_id)
            if not summary:
                print("Failed to generate summary.")
        else:
            print("Failed to fetch the transcript.")

if __name__ == "__main__":
    if len(sys.argv) < 1:
        print("Usage: python app.py <video_id>")
    else:
        print("= Sumaria =")
        video_id = sys.argv[1]
        start_time = time.time()
        Sumaria().run(video_id)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"in {elapsed_time:.2f} seconds")