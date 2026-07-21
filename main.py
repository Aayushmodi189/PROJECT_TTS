from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from tts import speak_text, get_voices

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):

    voices = get_voices()

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
            "voices": voices
        }
    )


@app.post("/speak")
def speak(
    text: str = Form(...),
    voice: int = Form(0),
    speed: int = Form(200),
    volume: int = Form(100)
):

    speak_text(text, voice, speed, volume)

    return RedirectResponse("/", status_code=303)