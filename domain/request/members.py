from typing import List, Any
from pydantic import BaseModel, validator


class GymClassReq(BaseModel):
    id: int
    name: str
    member_id: int
    trainer_id: int
    approved_id: int

    class Config:
        orm_mode = True


class ProfileMembersReq(BaseModel):
    id: int
    firstname: str
    lastname: str
    age: int
    height: float
    weight: float
    membership_type: str
    trainer_id: int

    gclass: List[int]

    # @validator("gclass", pre=True, allow_reuse=True, check_fields=False)
    # def gclass_set_to_list(cls, values):
    #     return [v.to_dict() for v in values]

    # @validator("trainer_id", pre=True, allow_reuse=True, check_fields=False)
    # def trainer_object_to_int(cls, values):
    #     if isinstance(values, int):
    #         return values
    #     else:
    #         return values.id.id

    # @validator("id", pre=True, allow_reuse=True, check_fields=False)
    # def member_id_to_int(cls, values):
    #     print(values)

    #     if isinstance(values, int):
    #         return values

    #     else:
    #         return values.id

    class Config:
        orm_mode = True
