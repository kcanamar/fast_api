##########################################
# * Import Dependencies
##########################################
from fastapi import APIRouter

# * Create Router
routes = APIRouter(prefix="")
##########################################
# * Setup Your Routes in This File
##########################################

@routes.get("/")
async def home():
    return {"home": "Welcome home"}