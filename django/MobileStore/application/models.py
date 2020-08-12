from django.db import models

# Create your models here.
class userdetails(models.Model):
    username_db = models.TextField(default="NA")
    location_db = models.TextField(default="NA")

    def __str__(self):
        return self.username_db + "*" + self.location_db