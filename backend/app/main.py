from typing import Any
from general import get_config
from fastapi import FastAPI, Request, HTTPException, Response
from fastapi.responses import HTMLResponse
import db
import json
from config import config
import users.main as users


data_provider: db.DataProvider = vars(db)[config.get("dataProvider")]()

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/api/user/")
async def get_user(request: Request):
    id = request.cookies.get("sessionKey")
    response = users.get_user(id)
    if not response:
        raise HTTPException(status_code=401, detail="User is unauthenticated")
    return response

@app.post("/api/user/login")
async def login(username: str, password: str, response: Response):
    #temp
    response.set_cookie("sessionKey", "123")
    return {"message": "Login successful"}

# student sends new lab
@app.put("/api/card/create")
async def create_card():
    raise NotImplementedError

@app.get("/api/cards")
async def cards_list():
    with open("./mockData.json") as file:
        return json.load(file)

# teacher gets preview numbers 

# teacher gets a lab

# teacher accepts, denies and leaves a comment to a lab request, otlozhenyye

# get labs tasks list
