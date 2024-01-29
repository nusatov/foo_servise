import uuid
from uuid import UUID

from django.db import models

from auth_app.models import CreatedUpdatedMixin, ServiceUser


class Order(CreatedUpdatedMixin):
    id: UUID = models.UUIDField(primary_key=True, default=uuid.uuid4)
    owner = models.ForeignKey(ServiceUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    category = models.CharField(max_length=50)
