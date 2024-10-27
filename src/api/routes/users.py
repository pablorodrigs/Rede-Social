#defineas rostas 


from fastapi import APIRouter

router = APIRouter(
    prefix="/Users",
    tags=["Users"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def home():
    return {'status': 'ok'}