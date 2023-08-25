import os
import openai

class OpenAIWrapper:
    def __init__(self):
        self.openai_api_key = os.getenv('OPENAI_API_KEY')
        openai.api_key = self.openai_api_key

    def extract_info(self, document):
        response = openai.Answer.create(
            search_model="davinci",
            documents=[document],
            question="Extract the player names, teams, golf club, city, state, course rating, scores, event information, and social profile URLs or other contact information.",
            stop=["\n"],
            max_tokens=500
        )
        return response.choices[0].text.strip()