from django.db import models

# Create your models here.
class userDetail(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    phoneno = models.CharField(max_length=20)
    ph_valid = models.IntegerField(default= 0)

    def __str__(self):
        return self.username

class OTPValidator(models.Model):
    otp = models.IntegerField()
    uid = models.IntegerField()
