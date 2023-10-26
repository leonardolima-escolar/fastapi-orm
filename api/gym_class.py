from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session
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
    repo: GymClassRepository = GymClassRepository(sess)

    gym_class = Gym_Class(
        id=req.id,
        name=req.name,
        member_id=req.member_id,
        trainer_id=req.trainer_id,
        approved_id=req.approved_id,
    )
    result = repo.insert_gym_class(gym_class)
    if result == True:
        return gym_class
    else:
        return JSONResponse(
            content={"message": "create gym class problem encountered"},
            status_code=500,
        )


@router.patch("/gym_class/update")
async def update_gym_class(id: int, req: GymClassReq, sess: Session = Depends(sess_db)):
    gym_class_dict = req.dict(exclude_unset=True)
    repo: GymClassRepository = GymClassRepository(sess)
    result = repo.update_gym_class(id, gym_class_dict)
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
    repo: GymClassRepository = GymClassRepository(sess)
    result = repo.delete_gym_class(id)
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
    repo: GymClassRepository = GymClassRepository(sess)
    result = repo.get_all_gym_class()
    return result


@router.get("/gym_class/get/{id}")
async def get_gym_class(id: int, sess: Session = Depends(sess_db)):
    repo: GymClassRepository = GymClassRepository(sess)
    result = repo.get_gym_class(id)
    return result
