from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pathlib import Path
from fastapi.staticfiles import StaticFiles


app = FastAPI()

Base_dir = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=(Base_dir / "templates"))

app.mount("/static", StaticFiles(directory=Base_dir/"static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})