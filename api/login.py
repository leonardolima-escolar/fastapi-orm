from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session
from cqrs.login.command.create_handlers import AddLoginCommandHandler
from cqrs.login.command.delete_handlers import DeleteLoginCommandHandler
from cqrs.login.command.update_handlers import UpdateLoginCommandHandler
from cqrs.login.commands import LoginCommand
from cqrs.login.queries import LoginListQuery, LoginRecordQuery
from cqrs.login.query.query_handlers import (
    ListLoginQueryHandler,
    RecordLoginQueryHandler,
)
from db_config.sqlalchemy_connect import SessionFactory
from domain.request.login import LoginReq
from domain.data.sqlalchemy_models import Login
from repository.sqlalchemy.login import LoginRepository
from typing import List

router = APIRouter()


def sess_db():
    db = SessionFactory()
    try:
        yield db
    finally:
        db.close()


@router.post("/login/add")
async def add_login(req: LoginReq, sess: Session = Depends(sess_db)):
    handler = AddLoginCommandHandler(sess)
    login = Login(
        id=req.id,
        username=req.username,
        password=req.password,
        date_approved=req.date_approved,
        user_type=req.user_type,
    )
    command = LoginCommand()
    command.details = login
    result = await handler.handle(command)
    if result == True:
        return login
    else:
        return JSONResponse(
            content={"message": "create login problem encountered"}, status_code=500
        )


@router.patch("/login/update")
async def update_login(id: int, req: LoginReq, sess: Session = Depends(sess_db)):
    handler = UpdateLoginCommandHandler(sess)
    login_dict = req.dict(exclude_unset=True)
    command = LoginCommand()
    command.details = login_dict
    result = await handler.handle(id, command)
    if result:
        return JSONResponse(
            content={"message": "login updated successfully"}, status_code=201
        )
    else:
        return JSONResponse(content={"message": "update login error"}, status_code=500)


@router.delete("/login/delete/{id}")
async def delete_login(id: int, sess: Session = Depends(sess_db)):
    handler = DeleteLoginCommandHandler(sess)
    command = LoginCommand()
    command.details["id"] = id
    result = await handler.handle(command)
    if result:
        return JSONResponse(
            content={"message": "login deleted successfully"}, status_code=201
        )
    else:
        return JSONResponse(content={"message": "delete login error"}, status_code=500)


@router.get("/login/list")
async def list_login(sess: Session = Depends(sess_db)):
    handler = ListLoginQueryHandler(sess)
    query: LoginListQuery = await handler.handle()
    return query.records


@router.get("/login/get/{id}")
async def get_login(id: int, sess: Session = Depends(sess_db)):
    handler = RecordLoginQueryHandler(sess)
    query: LoginRecordQuery = await handler.handle(id)
    return query.record
