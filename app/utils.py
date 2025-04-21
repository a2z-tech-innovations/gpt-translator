import openai
from sqlalchemy.orm import Session
from app.database.crud import update_translation_task
from dotenv import load_dotenv

import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

def perform_translation(task_id: int, text: str, languages: list, db: Session):
    translations = {}
    for lang in languages:
        try:
            response = openai.ChatCompletion.create(
                model = "gpt-4o-mini",
                messages=[
                    {"role": "system", "content": f"Translate the following text to {lang}:"},
                    {"role": "user", "content": text},
                ],
                max_tokens=1000
            )
            translated_text = response['choices'][0]['message']['content'].strip() # pyright: ignore
            translations[lang] = translated_text
        except Exception as e:
            print(f"Error translating text to {lang}: {e}")
            translations[lang] = f"Error: {e}"
    
    # Update the task with all translations at once
    update_translation_task(db, task_id, translations)
            