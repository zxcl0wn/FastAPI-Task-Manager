from fastapi import FastAPI
from .routes.users import router as user_router
from .routes.tasks import router as task_router
from .routes.categories import router as category_router
from .database import init_db


app = FastAPI()

app.include_router(user_router)
app.include_router(task_router)
app.include_router(category_router)

@app.get("/")
def test():
    return {
        "status": "OK"
    }

@app.on_event("startup")
def startup():
    init_db()
