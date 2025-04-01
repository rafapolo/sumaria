import requests
import re

class Summarizer:

    PROMPT_TEMPLATE = (
        "Summarize the following transcript into a clear, executive summary without an intro paragraph, "
        "with exactly 4 key bullet points in the same original language about what is discussed. "
        "Avoid notes, avoid quoting the reader, and instead paraphrase in concise academic language "
        "that captures the essence of the sentences. Do not refer to yourself, and do not explain your choices."
    )

    def prompt(self, text):
        model_url = "http://localhost:11434/api/generate"
        payload = {            
            "model": "gemma3",
            "stream": False,
            "prompt": text,
        }
        try:
            response = requests.post(model_url, json=payload)
            response.raise_for_status()
            summary = response.json().get("response", "")
            return summary
        except requests.exceptions.RequestException as e:
            print(f"Error communicating with the model: {e}")

    def summarize(self, transcript, video_id):
        chunk_size = 2000
        chunks = [transcript[i:i + chunk_size] for i in range(0, len(transcript), chunk_size)]
        print(f"ingesting {len(chunks)} chunks of {chunk_size} chars...")

        summaries = []
        for chunk in chunks:
        
            chunk_summary = self.prompt(f"{self.PROMPT_TEMPLATE} (Transcript: {chunk})")
            summaries.append(chunk_summary)            
            open(f"./cached/{video_id}/summary_chunk_{chunks.index(chunk)}.txt", "w").write(f"{chunk}\n-> summary ->\n{chunk_summary}")
        
        summary = '\n'.join(summaries)
        # clean up the summary
        summary = re.sub(r'Executive Summary:\s*', '', summary)
        summary = re.sub(r'(\*\s+.*?)\n{2,}(?=\*\s+)', r'\1\n', summary, flags=re.DOTALL)
        open(f"./cached/{video_id}/summary.txt", "w").write(summary)
        
        return summary