from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def str(self):
        return self.user.username
class MedicalStore(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    registration_number = models.CharField(max_length=20, unique=True)
    is_approved = models.BooleanField(default=False)