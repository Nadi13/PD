from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse

import users.main as users
from page_constructor.main import TestPageConstructor


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/test/", response_class=HTMLResponse)
async def test_page():
    return TestPageConstructor.construct()

@app.get("/api/user/")
async def get_user(request: Request):
    id = request.cookies.get("sessionKey")
    response = users.get_user(id)
    if not response:
        raise HTTPException(status_code=401, detail="User is not authentificated")
    return response