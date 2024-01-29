from django.db import models


class CreatedUpdatedMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class ServiceUser(CreatedUpdatedMixin):
    username = models.CharField(max_length=50, unique=True, db_index=True)
    email = models.EmailField(unique=True, db_index=True)
    password = models.CharField(max_length=256)
    token = models.CharField(max_length=256, unique=True, db_index=True)
    category = models.CharField(max_length=30)
    
    deleted = models.BooleanField(default=False)

