from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session
from cqrs.trainers.command.create_handlers import AddTrainerCommandHandler
from cqrs.trainers.command.delete_handlers import DeleteTrainerCommandHandler
from cqrs.trainers.command.update_handlers import UpdateTrainerCommandHandler
from cqrs.trainers.commands import ProfileTrainerCommand
from cqrs.trainers.queries import ProfileTrainerListQuery, ProfileTrainerRecordQuery
from cqrs.trainers.query.query_handlers import (
    ListTrainerQueryHandler,
    RecordTrainerQueryHandler,
)
from db_config.sqlalchemy_connect import SessionFactory
from domain.request.trainers import ProfileTrainersReq
from domain.data.sqlalchemy_models import Profile_Trainers
from repository.sqlalchemy.profile_trainers import ProfileTrainersRepository
from typing import List

router = APIRouter()


def sess_db():
    db = SessionFactory()
    try:
        yield db
    finally:
        db.close()


@router.post("/profile_trainers/add")
async def add_profile_trainers(
    req: ProfileTrainersReq, sess: Session = Depends(sess_db)
):
    handler = AddTrainerCommandHandler(sess)
    profile_trainers = Profile_Trainers(
        id=req.id,
        firstname=req.firstname,
        lastname=req.lastname,
        age=req.age,
        position=req.position,
        tenure=req.tenure,
        shift=req.shift,
    )
    command = ProfileTrainerCommand()
    command.details = profile_trainers
    result = await handler.handle(command)
    if result == True:
        return profile_trainers
    else:
        return JSONResponse(
            content={"message": "create profile trainers problem encountered"},
            status_code=500,
        )


@router.patch("/profile_trainers/update")
async def update_profile_trainers(
    id: int, req: ProfileTrainersReq, sess: Session = Depends(sess_db)
):
    handler = UpdateTrainerCommandHandler(sess)
    profile_trainers_dict = req.dict(exclude_unset=True)
    command = ProfileTrainerCommand()
    command.details = profile_trainers_dict
    result = await handler.handle(id, command)
    if result:
        return JSONResponse(
            content={"message": "profile trainers updated successfully"},
            status_code=201,
        )
    else:
        return JSONResponse(
            content={"message": "update profile trainers error"}, status_code=500
        )


@router.delete("/profile_trainers/delete/{id}")
async def delete_profile_trainers(id: int, sess: Session = Depends(sess_db)):
    handler = DeleteTrainerCommandHandler(sess)
    command = ProfileTrainerCommand()
    command.details["id"] = id
    result = await handler.handle(command)
    if result:
        return JSONResponse(
            content={"message": "profile trainers deleted successfully"},
            status_code=201,
        )
    else:
        return JSONResponse(
            content={"message": "delete profile trainers error"}, status_code=500
        )


@router.get("/profile_trainers/list")
async def list_profile_trainers(sess: Session = Depends(sess_db)):
    handler = ListTrainerQueryHandler(sess)
    query: ProfileTrainerListQuery = await handler.handle()
    return query.records


@router.get("/profile_trainers/get/{id}")
async def get_profile_trainers(id: int, sess: Session = Depends(sess_db)):
    handler = RecordTrainerQueryHandler(sess)
    query: ProfileTrainerRecordQuery = await handler.handle(id)
    return query.record
