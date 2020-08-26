from django.db import models

# Create your models here.
class events(models.Model):
    name_db = models.TextField(default="NA")
    place_db = models.TextField(default="NA")
    month_db = models.TextField(default="NA")
    year_db = models.TextField(default="NA")
    startingPrice_db = models.TextField(default="NA")
    maximumPrice_db = models.TextField(default="NA")
    customerName_db = models.TextField(default="NA")

    def __str__(self):
        return self.name_db + "*" + self.place_db + "*" + self.month_db + "*" + self.year_db + "*" + self.startingPrice_db + "*" + self.maximumPrice_db + "*" + self.customerName_db
