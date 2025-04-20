from fastapi import FastAPI, HTTPException, Request, Depends 
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

from fastapi.templating import Jinja2Templates
from app.database import schemas, crud, models

from app.database.db import get_db, engine

models.Base.metadata.create_all(bind=engine)
app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

# Configure CORS middleware
origins = [
    "http://localhost",
    "http://localhost:3000",
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
def translate(request: schemas.TranslationRequest, db = Depends(get_db)):
    translate_task = crud.create_translation_task(db, request.text, request.languages)
    return {"task_id": translate_task.id}

@app.get("/translate/{task_id}", response_class=HTMLResponse)
def get_translation_status(request: Request, task_id: int, db = Depends(get_db)):
    task = crud.get_translation_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Translation task not found")
    return templates.TemplateResponse("results.html", {
        "request": request,
        "task": task
    })
