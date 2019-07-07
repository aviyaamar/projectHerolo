from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Messages(models.Model):
    sender = models.ForeignKey(User, related_name="sender", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="receiver", on_delete=models.CASCADE)
    message = models.TextField()
    subject = models.CharField(max_length=255)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
      return self.sender+'  '+self.message


