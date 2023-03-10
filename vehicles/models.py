from django.db import models

# Create your models here.
class Vehicles(models.Model):
    name=models.CharField(max_length=200,default="name")
    brand=models.CharField(max_length=200,null=True)
    color=models.CharField(max_length=150,null=True)
    opt=(
        ("diesel","diesel"),
        ("petrol","petrol"),
        ("petrol","petrol"),
        ("petrol","petrol"),
        ("cng","cng"),
        ("ev","ev")
    )
    fuel_type=models.CharField(max_length=200,choices=opt,null=True)
    year=models.DateField(null=True)
    price=models.PositiveIntegerField(default=50000)
    runned_km=models.PositiveIntegerField(null=True)
    user=models.CharField(max_length=50)

    def __str__(self):
        return self.name

