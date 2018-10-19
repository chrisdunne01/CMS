from django.db import models

# Create your models here.

class Post(models.Model):
    user_id = models.CharField(max_length=25)
    user_description = models.TextField(max_length=25)
    FirstName = models.TextField(max_length=25)
    LastName = models.TextField(max_length=25)
    EmailAddress = models.TextField(max_length=50)
    Password = models.TextField(max_length=50)
    Group = models.TextField(max_length=50)

    def __str__(self):
        return self.user_id
