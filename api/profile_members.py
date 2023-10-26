from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session
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
    repo: ProfileMembersRepository = ProfileMembersRepository(sess)

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
    result = repo.insert_profile_members(profile_members)
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
    profile_members_dict = req.dict(exclude_unset=True)
    profile_members_dict.pop("gclass")
    repo: ProfileMembersRepository = ProfileMembersRepository(sess)
    result = repo.update_profile_members(id, profile_members_dict)
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
    repo: ProfileMembersRepository = ProfileMembersRepository(sess)
    result = repo.delete_profile_members(id)
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
    repo: ProfileMembersRepository = ProfileMembersRepository(sess)
    result = repo.get_all_profile_members()
    return result


@router.get("/profile_members/get/{id}")
async def get_profile_members(id: int, sess: Session = Depends(sess_db)):
    repo: ProfileMembersRepository = ProfileMembersRepository(sess)
    result = repo.get_profile_members(id)
    return result
