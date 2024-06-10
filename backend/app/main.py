from typing import Annotated, Any, Sequence, Type, TypeAlias
from fastapi import FastAPI, Request, HTTPException, Response, Body, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from cards.objects import Card, CreatedCard, FullCard
import db
from config import config
import users.main as users
import cards.main as cards
from icecream import ic
from users.objects import *
from sessions import SessionManager
from sqlalchemy.ext.asyncio import AsyncSession


data_provider: Type[db.DataProvider]
sessionmanager: SessionManager

def __initialize() -> None:
    global data_provider
    global sessionmanager

    providerType: type = config["dataProvider"]
    session_manager_parameters: dict[str, Any] = config.get("sessionManagerParameters", dict())
    secrets: dict[str, str] = config["secrets"].get("sessionManager", {})
    sessionmanager = SessionManager(**session_manager_parameters, **secrets)
    data_provider = vars(db)[providerType]()

__initialize()

DBSession: TypeAlias  = Annotated[AsyncSession, Depends(sessionmanager.with_session)]

app = FastAPI()

app.add_middleware( # to reconsider
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return HTMLResponse('''
<html>
    <head>
        <title>Some HTML in here</title>
    </head>
    <body>
        <h1>test</h1>
    </body>
</html>
''')


@app.get("/api/user")
async def get_user(sessionKey: str, session: DBSession) -> User:
    response = await users.get(sessionKey, session, data_provider)
    if not response:
        raise HTTPException(status_code=401, detail="User is unauthenticated")
    return response

@app.post("/api/user/register")
async def register_user(session: DBSession, user: RegistrationEntity = Body()) -> str:
    response = await users.add(user, session, data_provider)
    if response == "Invalid value":
        raise HTTPException(status_code=400, detail=response)
    if response == "Internal error":
        raise HTTPException(status_code=500, detail=response)
    return response

@app.post("/api/user/login")
async def login(user: UserCredentials, response: Response) -> dict[str, Any]:
    #temp
    # response.set_cookie("sessionKey", "123")
    return {"message": "Login successful"}

# student sends new lab
@app.put("/api/card/create", status_code=201)
async def create_card(session: DBSession, card: Card = Body()) -> str:
    response = await cards.add(card, session, data_provider)
    if response == "Invalid value":
        raise HTTPException(status_code=400, detail=response)
    if response == "Internal error":
        raise HTTPException(status_code=500, detail=response)
    return response

# teacher gets labs list
@app.get("/api/cards")
async def cards_list(sessionKey: str, session: DBSession) -> Sequence[FullCard]:
    user = await users.get(sessionKey, session, data_provider)
    if not user:
        raise HTTPException(status_code=401, detail="User is unauthenticated")
    response = await cards.get_all(data_provider, session)
    return response

# teacher gets preview numbers
@app.get("/api/overview")
async def overview():
    raise NotImplementedError

# teacher gets a lab
@app.get("/api/card")
async def get_card(sessionKey: str, id: int, session: DBSession) -> FullCard:
    user = await users.get(sessionKey, session, data_provider)
    if not user:
        raise HTTPException(status_code=401, detail="User is unauthenticated")
    response = await cards.get(id, session, data_provider)
    if not response:
        raise HTTPException(status_code=400, detail="Card does not exist")
    return response

# teacher accepts, denies and leaves a comment to a lab request, otlozhenyye
@app.put("/api/card/update")
async def update_card():
    raise NotImplementedError
