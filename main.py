import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/assets", StaticFiles(directory="assets"), name="assets")

@app.get("/index/", response_class=HTMLResponse)
async def table(request: Request):
    response = templates.TemplateResponse("test3.html", {"request": request}) 
    return response
