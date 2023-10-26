from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session
from cqrs.attendance.queries import AttendanceListQuery
from cqrs.attendance.query.query_handlers import ListAttendanceQueryHandler
from cqrs.signup.command.create_handlers import AddSignupCommandHandler
from cqrs.signup.command.delete_handlers import DeleteSignupCommandHandler
from cqrs.signup.command.update_handlers import UpdateSignupCommandHandler
from cqrs.signup.commands import SignupCommand
from cqrs.signup.queries import SignupListQuery, SignupRecordQuery
from cqrs.signup.query.query_handlers import (
    ListSignupQueryHandler,
    RecordSignupQueryHandler,
)
from db_config.sqlalchemy_connect import SessionFactory
from domain.request.signup import SignupReq
from domain.data.sqlalchemy_models import Signup
from repository.sqlalchemy.signup import (
    SignupRepository,
    LoginMemberRepository,
    MemberAttendanceRepository,
)
from typing import List

router = APIRouter()


def sess_db():
    db = SessionFactory()
    try:
        yield db
    finally:
        db.close()


@router.post("/signup/add")
async def add_signup(req: SignupReq, sess: Session = Depends(sess_db)):
    handler = AddSignupCommandHandler(sess)
    signup = Signup(password=req.password, username=req.username, id=req.id)
    command = SignupCommand()
    command.details = signup
    result = await handler.handle(command)
    if result == True:
        return signup
    else:
        return JSONResponse(
            content={"message": "create signup problem encountered"}, status_code=500
        )


@router.get("/signup/list", response_model=List[SignupReq])
async def list_signup(sess: Session = Depends(sess_db)):
    handler = ListSignupQueryHandler(sess)
    query: SignupListQuery = await handler.handle()
    return query.records


@router.patch("/signup/update")
async def update_signup(id: int, req: SignupReq, sess: Session = Depends(sess_db)):
    handler = UpdateSignupCommandHandler(sess)
    signup_dict = req.dict(exclude_unset=True)
    command = SignupCommand()
    command.details = signup_dict
    result = await handler.handle(id, command)
    if result:
        return JSONResponse(
            content={"message": "profile updated successfully"}, status_code=201
        )
    else:
        return JSONResponse(
            content={"message": "update profile error"}, status_code=500
        )


@router.delete("/signup/delete/{id}")
async def delete_signup(id: int, sess: Session = Depends(sess_db)):
    handler = DeleteSignupCommandHandler(sess)
    command = SignupCommand()
    command.details["id"] = id
    result = await handler.handle(command)
    if result:
        return JSONResponse(
            content={"message": "profile deleted successfully"}, status_code=201
        )
    else:
        return JSONResponse(
            content={"message": "delete profile error"}, status_code=500
        )


@router.get("/signup/list/{id}", response_model=SignupReq)
async def get_signup(id: int, sess: Session = Depends(sess_db)):
    handler = RecordSignupQueryHandler(sess)
    query: SignupRecordQuery = await handler.handle(id)
    return query.record


@router.get("/login/memberslist")
def get_join_login_members(sess: Session = Depends(sess_db)):
    repo: LoginMemberRepository = LoginMemberRepository(sess)
    result = repo.join_login_members()
    return result


@router.get("/member/attendance")
async def get_join_member_attendance(sess: Session = Depends(sess_db)):
    handler = ListAttendanceQueryHandler(sess)
    query: AttendanceListQuery = await handler.handle()
    return query.records
