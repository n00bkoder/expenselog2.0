from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()




class Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.CharField(max_length=50)
    cost = models.DecimalField(max_digits=11, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
