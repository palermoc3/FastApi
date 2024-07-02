from fastapi import ApiRouter
from workout_api.atleta.controller import routes as atleta

api_router = ApiRouter()
api_router.include_router(atleta, prefix = 'atletas', taggs=['atletas/'])