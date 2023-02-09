from django.db import models

# Create your models here.


class User(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    age = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstName + " " + self.lastName


class UserDetail(models.Model):
    phoneNo = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    user = models.OneToOneField(User, related_name="user", on_delete=models.CASCADE)
