import re
import requests
from semantic_tokenizer import SemanticTokenizer
import json

class Summarizer:

    def prompt(self, text):
        model_url = "http://localhost:11434/api/generate"
        payload = {            
            "model": "mistral:instruct",
            "stream": False,
            "prompt": text,
            "options": {
                "temperature": 0.7,
                "top_p": 0.9,
                "num_predict": 512  # Equivalent to max_new_tokens
            }
        }
        try:
            response = requests.post(model_url, json=payload)
            response.raise_for_status()
            return response.json().get("response", "")
        except requests.exceptions.RequestException as e:
            print(f"Error communicating with the model: {e}")

    def summarize(self, transcript, video_id):
        summary = self.prompt(
            "Have a 4 line summary of the video transcript and extract the 4 main themes in this transcript:\n\n"
            f"{transcript}\n\n"
            "Format:\n"
            "{\n"
            "  \"line-summary\": \"Example summary\"},\n"
            "  \"themes\": [\n"
            "    { \"title\": \"Example Theme\"},\n"
            "    ...\n"
            "  ]\n"
            "}"
        )

        try:
            themes = json.loads(summary).get("themes", [])
            one_line = json.loads(summary).get("line-summary", "")
        except json.JSONDecodeError as e:
            print(f"Error parsing summary as JSON: {e}")
            themes = []
        
        summaries = [one_line]
        for theme in themes:            
            title = theme.get("title", "")
            print(title)
            theme_summary = self.prompt(
                f"Summarize the theme: \"{title}\" from this transcript. Use 3–5 bullet points. Be specific."
            )
            summaries.append(f"### {title}\n\n{theme_summary}")

        summary = "\n\n".join(summaries)
        open(f"./cached/{video_id}/summary.md", "w").write(summary)
        
        return summary