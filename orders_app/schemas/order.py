from uuid import UUID

from ninja import Schema


class OrderCreateSchema(Schema):
    name: str
    description: str
    category: str


class CreatedOrderResponseSchema(Schema):
    id: UUID
    owner: str
    name: str
    description: str
    category: str
