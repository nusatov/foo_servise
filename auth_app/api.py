import os
import random
import string

from django.contrib.auth.hashers import make_password, check_password
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from ninja import NinjaAPI, Router
from ninja.errors import AuthenticationError
from ninja.security import APIKeyHeader

from auth_app.models import ServiceUser
from auth_app.schemas.errors import Error
from auth_app.schemas.user import UserRegisterSchema, UserSchema, UserLoginResponseSchema, UserLoginSchema

router = Router()



@router.post('/signup', response={201: UserSchema, 409: Error})
def signup(request, register_user: UserRegisterSchema):
    user_dto = register_user.model_dump()
    if len(user_dto['password']) < 8:
        return 409, {'message': 'Password must be at least 8 characters long'}
    user_dto['password'] = make_password(user_dto['password'])
    user_dto['token'] = create_token()
    del user_dto['password_repeat']
    print(user_dto)
    try:
        new_user = ServiceUser.objects.create(**user_dto)
    except IntegrityError:
        return 409, {'message': 'Username or email already exists'}
    
    return 201, new_user


def create_token():
    length = int(os.getenv('TOKEN_LENGTH'))
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(length))


@router.post('/login', response={200: UserLoginResponseSchema, 401: Error})
def login(request, login_user: UserLoginSchema):
    try:
        user = ServiceUser.objects.get(username=login_user.username)
    except ObjectDoesNotExist:
        return 401, {'message': 'Username or password is incorrect'}
    
    if not check_password(login_user.password, user.password):
        return 401, {'message': 'Username or password is incorrect'}
    
    return user


class ApiKey(APIKeyHeader):
    param_name = "Authorization"
    
    def authenticate(self, request, key):
        try:
            username, token = key.split()
            user = ServiceUser.objects.get(username=username)
        except (AttributeError, ObjectDoesNotExist):
            raise AuthenticationError
        if user.token == token:
            return key


header_key = ApiKey()


@router.get("/private_api", auth=header_key)
def apikey(request):
    return {'message': 'You have got an protected data'}
