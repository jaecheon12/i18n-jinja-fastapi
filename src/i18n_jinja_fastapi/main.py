from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles 
from fastapi.templating import Jinja2Templates
from babel.plural import PluralRule
import glob
import json
import jinja2
import os  # os 모듈을 임포트합니다.
from core.config import settings
from core.utils import get_gettext_translations
from icecream import ic

app = FastAPI(title=settings.PROJECT_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

default_locale = 'en'
languages = {}

language_list = glob.glob("src/static/languages/*.json")

ic(language_list)

for lang in language_list:
    # os.path를 사용하여 파일 이름을 안전하게 처리합니다.
    filename = os.path.basename(lang)
    ic(filename)
    lang_code = filename.split('.')[0]
    with open(lang, 'r', encoding='utf8') as file:
        languages[lang_code] = json.load(file)

templates = Jinja2Templates(directory="src/templates")
app.mount("/static", StaticFiles(directory="src/static"), name="static")
        
@app.get("/rental/{locale}", response_class=HTMLResponse)
async def rental(request: Request, locale: str):
    if(locale not in languages):
        locale = default_locale
    result = {"request": request}
    result.update(languages[locale])
    result.update({'locale': locale, 'bedroom_value': 2})
    result.update({'rent_per_month': 300}) # dynamic values
    return templates.TemplateResponse("index.html", result)

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/index")
async def index():
    return {"message": f"Hello i18n-jinja-fastapi"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=settings.PROJECT_PORT, reload=True)