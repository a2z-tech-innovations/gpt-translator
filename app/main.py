from fastapi import BackgroundTasks, FastAPI, HTTPException, Request, Depends 
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

from fastapi.templating import Jinja2Templates
from app.database import schemas, crud, models

from app.database.db import get_db, engine, SessionLocal
from typing import List
import uuid
from app.utils import perform_translation

models.Base.metadata.create_all(bind=engine)
app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

# Configure CORS middleware
origins = [
    "http://localhost",
    "http://0.0.0.0",
    "http://0.0.0.0:8000",
    "http://localhost:8000",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/index", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
    

@app.post("/translate", response_model=schemas.TaskResponse)
def translate_text(request: schemas.TranslationRequest,background_tasks: BackgroundTasks, db = Depends(get_db)):
    translate_task = crud.create_translation_task(db, request.text, request.languages)
    # Convert Column to int
    task_id = int(translate_task.id) # pyright: ignore
    background_tasks.add_task(perform_translation, task_id, request.text, request.languages, db)
    return {"task_id": translate_task.id}

@app.get("/translate/{task_id}", response_class=HTMLResponse)
def get_translate(request: Request, task_id: int, db = Depends(get_db)):
    translate_task = crud.get_translation_task(db, task_id)
    if not translate_task:
        raise HTTPException(status_code=404, detail="Translation task not found")
    return templates.TemplateResponse("results.html", {
        "request": request,
        "task": translate_task
    })
 
@app.get("/translate/content/{task_id}")
def get_translate_content(request: Request, task_id: int, db = Depends(get_db)):
    translate_task = crud.get_translation_task(db, task_id)
    if not translate_task:
        raise HTTPException(status_code=404, detail="Translation task not found")
    return translate_task