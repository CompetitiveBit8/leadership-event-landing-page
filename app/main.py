from fastapi import FastAPI, Request, Form, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pathlib import Path
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from routers.schemas import comments
from routers.database import Base, SessionLocal, engine, get_db
from routers.models import feedback


app = FastAPI()

Base_dir = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=(Base_dir / "templates"))

app.mount("/static", StaticFiles(directory=Base_dir/"static"), name="static")

Base.metadata.create_all(bind=engine)

@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/feedback")
async def participantFeedback(request: Request, name: str = Form(...),
                                email: str = Form(...),
                                subject: str = Form(...),
                                message: str = Form(...),
                                db : Session = Depends(get_db)
                                ):
    new_feedback = feedback(name=name, email=email, subject=subject, message=message)
    db.add(new_feedback)
    db.commit()
    db.refresh(new_feedback)
    return {"message": "User feedback updated", "Feedback":{"name":new_feedback.name, "email":new_feedback.email, "subject":new_feedback.subject, "message":new_feedback.message} }


