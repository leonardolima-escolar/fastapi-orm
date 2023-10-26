from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session
from cqrs.members.command.create_handlers import AddMemberCommandHandler
from cqrs.members.command.delete_handlers import DeleteMemberCommandHandler
from cqrs.members.command.update_handlers import UpdateMemberCommandHandler
from cqrs.members.commands import ProfileMemberCommand
from cqrs.members.queries import ProfileMemberListQuery, ProfileMemberRecordQuery
from cqrs.members.query.query_handlers import (
    ListMemberQueryHandler,
    RecordMemberQueryHandler,
)
from db_config.sqlalchemy_connect import SessionFactory
from domain.request.members import ProfileMembersReq
from domain.data.sqlalchemy_models import Profile_Members
from repository.sqlalchemy.profile_members import ProfileMembersRepository
from typing import List

router = APIRouter()


def sess_db():
    db = SessionFactory()
    try:
        yield db
    finally:
        db.close()


@router.post("/profile_members/add")
async def add_profile_members(req: ProfileMembersReq, sess: Session = Depends(sess_db)):
    handler = AddMemberCommandHandler(sess)

    profile_members = Profile_Members(
        id=req.id,
        firstname=req.firstname,
        lastname=req.lastname,
        age=req.age,
        height=req.height,
        weight=req.weight,
        membership_type=req.membership_type,
        trainer_id=req.trainer_id,
    )
    command = ProfileMemberCommand()
    command.details = profile_members
    result = await handler.handle(command)
    if result == True:
        return profile_members
    else:
        return JSONResponse(
            content={"message": "create profile members problem encountered"},
            status_code=500,
        )


@router.patch("/profile_members/update")
async def update_profile_members(
    id: int, req: ProfileMembersReq, sess: Session = Depends(sess_db)
):
    handler = UpdateMemberCommandHandler(sess)
    profile_members_dict = req.dict(exclude_unset=True)
    command = ProfileMemberCommand()
    command.details = profile_members_dict
    result = await handler.handle(id, command)
    if result:
        return JSONResponse(
            content={"message": "profile members updated successfully"},
            status_code=201,
        )
    else:
        return JSONResponse(
            content={"message": "update profile members error"}, status_code=500
        )


@router.delete("/profile_members/delete/{id}")
async def delete_profile_members(id: int, sess: Session = Depends(sess_db)):
    handler = DeleteMemberCommandHandler(sess)
    command = ProfileMemberCommand()
    command.details["id"] = id
    result = await handler.handle(command)
    if result:
        return JSONResponse(
            content={"message": "profile members deleted successfully"},
            status_code=201,
        )
    else:
        return JSONResponse(
            content={"message": "delete profile members error"}, status_code=500
        )


@router.get("/profile_members/list")
async def list_profile_members(sess: Session = Depends(sess_db)):
    handler = ListMemberQueryHandler(sess)
    query: ProfileMemberListQuery = await handler.handle()
    return query.records


@router.get("/profile_members/get/{id}")
async def get_profile_members(id: int, sess: Session = Depends(sess_db)):
    handler = RecordMemberQueryHandler(sess)
    query: ProfileMemberRecordQuery = await handler.handle(id)
    return query.record
