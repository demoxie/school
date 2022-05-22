import datetime

from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from starlette import status
from starlette.exceptions import HTTPException
from starlette.responses import JSONResponse

from src.models import user_model
from src.models.user_model import Student, Student_pydantic
from src.schemas.user_schema import UserSignupSchema

common_router = APIRouter()


@common_router.post("/signup")
async def student_signup(user: UserSignupSchema):
    db_user = await user_model.Student.get_or_none(username=user.username)
    if db_user is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exist"
        )

    user_info = user.dict(exclude_unset=True)
    user_info["date_of_birth"] = datetime.datetime.strptime(user.date_of_birth, '%Y-%m-%d')
    # user_info["password"] = Auth.get_password_hash(user_info["password"])
    user_obj = await Student.create(**user_info)
    # token_obj = Auth.create_signup_confirmation_token(user_obj.id)
    # print(token_obj)

    # user_obj.confirmation = token_obj.get("jti")

    # try:
    #     mail_template = EmailTemplate("Account Confirmation", user.name, "Zumaridi", user.name, user.email, [""],
    #                                   token_obj["token"])
    #     print(await Mailer.send_signup_mail(mail_template))
    # except ConnectionRefusedError:
    #
    #     raise HTTPException(
    #         status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    #         detail="Email couldn't be send. Please try again..."
    #     )

    await user_obj.save()
    db_user = await Student_pydantic.from_tortoise_orm(user_obj)
    json_compatible_item_data = jsonable_encoder(db_user)

    return JSONResponse(content=json_compatible_item_data)


@common_router.post("/login")
async def login():
    return "welcome oh"
