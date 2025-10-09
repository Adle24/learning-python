from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


app = FastAPI()

app.mount("/.", StaticFiles(directory="./"), name="")

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def home(thing:str, height: str, color:str, request: Request, response: HTMLResponse):
    return templates.TemplateResponse(request=request, name="home.html", context={"thing": thing, "height": height, "color": color})
