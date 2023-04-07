from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from worker import tasks
from uuid import uuid4


templates = Jinja2Templates(directory="client/templates")


def create_app(debug=True):
    app = FastAPI()
    app.debug = debug

    @app.get("/", response_class=HTMLResponse)
    def get_root(request: Request):
        return templates.TemplateResponse("index.html", context={ "request": request })
    
    @app.post("/", response_class=HTMLResponse)
    def post_root(request: Request):
        for _ in range(50):
            tasks.logging.delay()
        return RedirectResponse(url=f"/tasks/{123}", status_code=301)
    
    @app.get("/tasks/{task_id}", response_class=HTMLResponse)
    def get_task(request: Request, task_id: str):
        return templates.TemplateResponse("task.html", context={ "request": request, "task_id": task_id }) 
    
    return app