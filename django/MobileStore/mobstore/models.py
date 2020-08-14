from django.db import models

# Create your models here.
class mobile(models.Model):
    modelno_db = models.TextField(default="NA")
    price_db = models.TextField(default="NA")
    year_db = models.TextField(default="NA")
    company_db = models.TextField(default="NA")
    RAM_db = models.TextField(default="NA")
    ROM_db = models.TextField(default="NA")

    def __str__(self):
        return self.modelno_db + "*" + self.price_db + "*" + self.year_db + "*" + self.company_db + "*" + self.RAM_db + "*" + self.ROM_db

