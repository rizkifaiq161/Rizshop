from django.db import models
import uuid  # tambahkan baris ini di paling atas
from django.contrib.auth.models import User


# Create your models here.
class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # tambahkan baris ini
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    description = models.TextField()
    amount = models.IntegerField()
 
