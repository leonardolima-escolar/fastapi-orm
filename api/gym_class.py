from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session
from cqrs.gym_class.command.create_handlers import AddGymClassCommandHandler
from cqrs.gym_class.command.delete_handlers import DeleteGymClassCommandHandler
from cqrs.gym_class.command.update_handlers import UpdateGymClassCommandHandler
from cqrs.gym_class.commands import GymClassCommand
from cqrs.gym_class.queries import GymClassListQuery, GymClassRecordQuery
from cqrs.gym_class.query.query_handlers import (
    ListGymClassQueryHandler,
    RecordGymClassQueryHandler,
)
from db_config.sqlalchemy_connect import SessionFactory
from domain.request.members import GymClassReq
from domain.data.sqlalchemy_models import Gym_Class
from repository.sqlalchemy.gym_class import GymClassRepository
from typing import List

router = APIRouter()


def sess_db():
    db = SessionFactory()
    try:
        yield db
    finally:
        db.close()


@router.post("/gym_class/add")
async def add_gym_class(req: GymClassReq, sess: Session = Depends(sess_db)):
    handler = AddGymClassCommandHandler(sess)
    gym_class = Gym_Class(
        id=req.id,
        name=req.name,
        member_id=req.member_id,
        trainer_id=req.trainer_id,
        approved_id=req.approved_id,
    )
    command = GymClassCommand()
    command.details = gym_class
    result = await handler.handle(command)
    if result == True:
        return gym_class
    else:
        return JSONResponse(
            content={"message": "create gym class problem encountered"},
            status_code=500,
        )


@router.patch("/gym_class/update")
async def update_gym_class(id: int, req: GymClassReq, sess: Session = Depends(sess_db)):
    handler = UpdateGymClassCommandHandler(sess)
    gym_class_dict = req.dict(exclude_unset=True)
    command = GymClassCommand()
    command.details = gym_class_dict
    result = await handler.handle(id, command)
    if result:
        return JSONResponse(
            content={"message": "gym class updated successfully"},
            status_code=201,
        )
    else:
        return JSONResponse(
            content={"message": "update gym class error"}, status_code=500
        )


@router.delete("/gym_class/delete/{id}")
async def delete_gym_class(id: int, sess: Session = Depends(sess_db)):
    handler = DeleteGymClassCommandHandler(sess)
    command = GymClassCommand()
    command.details["id"] = id
    result = await handler.handle(command)
    if result:
        return JSONResponse(
            content={"message": "gym class deleted successfully"},
            status_code=201,
        )
    else:
        return JSONResponse(
            content={"message": "delete gym class error"}, status_code=500
        )


@router.get("/gym_class/list")
async def list_gym_class(sess: Session = Depends(sess_db)):
    handler = ListGymClassQueryHandler(sess)
    query: GymClassListQuery = await handler.handle()
    return query.records


@router.get("/gym_class/get/{id}")
async def get_gym_class(id: int, sess: Session = Depends(sess_db)):
    handler = RecordGymClassQueryHandler(sess)
    query: GymClassRecordQuery = await handler.handle(id)
    return query.record
