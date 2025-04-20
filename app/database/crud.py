from sqlalchemy.orm import Session
from app.database import models



def create_translation_task(db: Session, text: str, languages: list):
    translation_task = models.TranslationTask(text=text, languages=languages)
    db.add(translation_task)
    db.commit()
    db.refresh(translation_task)
    return translation_task
    
def get_translation_task(db: Session, task_id: int):
    return db.query(models.TranslationTask).filter(models.TranslationTask.id == task_id).first()

def update_translation_task(db: Session, task_id: int, translations: dict):
    translation_task = db.query(models.TranslationTask).filter(models.TranslationTask.id == task_id).first()
    if translation_task:
        # Use setattr to update the columns
        setattr(translation_task, 'translations', translations)
        setattr(translation_task, 'status', 'completed')
        db.commit()
        db.refresh(translation_task)
    return translation_task