from fastapi import ApiRouter

router = ApiRouter()

@router.post(path='/')
async def post():
    pass