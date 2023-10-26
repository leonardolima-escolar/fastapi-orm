from fastapi import FastAPI
from api import admin, login, profile_trainers, profile_members, gym_class


app = FastAPI()
app.include_router(admin.router)
app.include_router(login.router)
app.include_router(profile_trainers.router)
app.include_router(profile_members.router)
app.include_router(gym_class.router)
