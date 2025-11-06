from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pathlib

app = FastAPI(title="Katana Drift")

# Путь к корню проекта (на случай запуска из другой директории)
BASE_DIR = pathlib.Path(__file__).resolve().parent.parent

# Монтируем статику
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
