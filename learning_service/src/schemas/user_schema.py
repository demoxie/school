from typing import Optional

from pydantic.main import BaseModel


class UserSignupSchema(BaseModel):
    first_name: str
    middle_name: Optional[str]
    last_name: str
    gender: str
    date_of_birth: Optional[str]
    address: Optional[str]
    username: str
    password: str

    class Config:
        orm_mode = True


# class ProfileUpdateSchema(BaseModel):
#     name: str
#     avatar: Optional[str]
#     country_of_origin: Optional[str]
#     profession: Optional[str]
#     language: Optional[str]
#     gender: Optional[str]
#     date_of_birth: Optional[str]
#     mobilePhone: Optional[str]
#
#     class Config:
#         orm_mode = True
#
#
# class LoginSchema(BaseModel):
#     email: str
#     password: str
#
#     class Config:
#         orm_mode = True
#

# class GoogleSignupSchema(BaseModel):
#     name: Optional[str]
#     familyName: str
#     givenName: str
#     googleId: str
#     imageUrl: Optional[str]
#     email: str
#
#     class Config:
#         orm_mode = True
#
#
# class GoogleLoginSchema(BaseModel):
#     name: Optional[str]
#     familyName: str
#     givenName: str
#     googleId: str
#     imageUrl: Optional[str]
#     email: str
#
#     class Config:
#         orm_mode = True
#
#
# class LinkedInInputSchema(BaseModel):
#     first_name: str
#     last_name: str
#     user_id: str
#     email: EmailStr
#
#     class Config:
#         orm_mode = True
#
#
# class MicrosoftInputSchema(BaseModel):
#     displayName: str
#     givenName: Optional[str]
#     surname: str
#     mobilePhone: Optional[str]
#     mail: Optional[str]
#     userPrincipalName: Optional[str]
#
#     class Config:
#         orm_mode = True
