from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class TimestampMixin:
    created_at = fields.DatetimeField(null=True, auto_now_add=True)
    modified_at = fields.DatetimeField(null=True)


class BankDetails(TimestampMixin, models.Model):
    id = fields.UUIDField(pk=True, auto_generate=True)
    account_name = fields.CharField(max_length=100, null=False)
    account_number = fields.CharField(max_length=15, null=False)
    bank_name = fields.TextField(max_length=50, null=False)
    account_type = fields.CharField(max_length=20, null=False)
    owner: fields.ReverseRelation['Staff']


class Role(TimestampMixin, models.Model):
    id = fields.UUIDField(pk=True, auto_generate=True)
    name = fields.CharField(max_length=100)

    class Meta:
        table = "role"


class UserModel(models.Model):
    id = fields.UUIDField(pk=True, auto_generate=True)
    first_name = fields.CharField(max_length=100, null=False)
    middle_name = fields.CharField(max_length=100, null=True)
    last_name = fields.CharField(max_length=100, null=False)
    gender = fields.CharField(max_length=20, null=False)
    date_of_birth = fields.DatetimeField(null=True)
    address = fields.TextField(max_length=250, null=True)
    username = fields.CharField(max_length=250, null=True, unique=True)
    password = fields.CharField(max_length=250, null=True)

    class Meta:
        abstract = True


class Student(TimestampMixin, UserModel):
    guardian_email = fields.CharField(max_length=200, null=True, unique=True)
    guardian_phone = fields.CharField(max_length=15, null=True)

    class Meta:
        table = "student"


class Staff(TimestampMixin, UserModel):
    phone_number = fields.CharField(max_length=15, null=True)
    roles = fields.ManyToManyField('models.Role', related_name='roles', through='staff_roles')
    bank_details = fields.ManyToManyField('models.BankDetails', related_name='bank_details',
                                          through='staff_bank_details')


Student_pydantic = pydantic_model_creator(Student, name="Student")
Staff_pydantic = pydantic_model_creator(Staff, name="Staff")
Role_pydantic = pydantic_model_creator(Staff, name="Staff")


