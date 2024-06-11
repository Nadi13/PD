from typing import Annotated, Any, Sequence, Type, TypeAlias
from fastapi import FastAPI, Header, Request, HTTPException, Response, Body, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from cards.objects import Card, CardQuery, CardUpdate, CreatedCard, FullCard
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
SessionKeyHeader: TypeAlias = Annotated[str | None, Header()]
Message: TypeAlias = dict[str, str]

app = FastAPI(root_path="/api")

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


@app.get("/user")
async def get_user(sessionKey: str, session: DBSession) -> User:
    response = await users.get(sessionKey, session, data_provider)
    if not response:
        raise HTTPException(status_code=401, detail="User is unauthenticated")
    return response

@app.post("/user/register")
async def register_user(session: DBSession, user: RegistrationEntity = Body()) -> str:
    response = await users.add(user, session, data_provider)
    if response == "Invalid value":
        raise HTTPException(status_code=400, detail=response)
    if response == "Internal error":
        raise HTTPException(status_code=500, detail=response)
    return response

@app.post("/user/login")
async def login(user: UserCredentials, session: DBSession) -> Message | SessionKey:
    response = await users.get_by_credentials(user, session, data_provider)
    if response in ["Invalid value", "Nonexistent value"]:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=response)
    session_key = await users.get_new_session(user, session, data_provider)
    return session_key

@app.put("/card/create", status_code=201)
async def create_card(session: DBSession, card: Card = Body(), sessionKey: SessionKeyHeader = None) -> str:
    user = await users.get(sessionKey, session, data_provider)
    if not user:
        raise HTTPException(status_code=401, detail="User is unauthenticated")
    response = await cards.add(card, session, data_provider)
    if response == "Invalid value":
        raise HTTPException(status_code=400, detail=response)
    if response == "Internal error":
        raise HTTPException(status_code=500, detail=response)
    return response

@app.get("/cards")
async def cards_list(sessionKey: str, session: DBSession) -> Sequence[FullCard]:
    user = await users.get(sessionKey, session, data_provider)
    if not user:
        raise HTTPException(status_code=401, detail="User is unauthenticated")
    response = await cards.get_all(data_provider, session)
    return response

@app.get("/overview")
async def overview():
    raise NotImplementedError

@app.get("/card")
async def get_card(session: DBSession, sessionKey: str, card: Annotated[CardQuery, Depends()]) -> Sequence[FullCard]:
    user = await users.get(sessionKey, session, data_provider)
    if not user:
        raise HTTPException(status_code=401, detail="User is unauthenticated")
    response = await cards.get(card, session, data_provider)
    if not response:
        raise HTTPException(status_code=400, detail="Card does not exist")
    return response

@app.patch("/card/update", status_code=status.HTTP_200_OK)
async def update_card(update: CardUpdate, session: DBSession, sessionKey: SessionKeyHeader = None) -> str:
    user = await users.get(sessionKey, session, data_provider)
    if not user:
        raise HTTPException(status_code=401, detail="User is unauthenticated")
    response = await cards.update(update, session, data_provider)
    return response

@app.get("/groups", status_code=status.HTTP_200_OK)
async def get_groups(session: DBSession) -> Sequence[Group]:
    groups = await users.get_all_groups(session, data_provider)
    return groups
