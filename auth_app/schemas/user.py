from ninja import Schema


class UserRegisterSchema(Schema):
    username: str
    email: str
    password: str
    password_repeat: str
    category: str


class UserSchema(Schema):
    username: str
    email: str
    category: str


class UserLoginSchema(Schema):
    username: str
    password: str


class UserLoginResponseSchema(Schema):
    username: str
    email: str
    category: str
    token: str


class PrivateRequestSchema(Schema):
    username: str
    token: str
