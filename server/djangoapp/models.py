from django.db import models
from django.utils.timezone import now

# Create your models here.

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Add any other fields you want for CarMake model

    def __str__(self):
        return self.name


class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dealer_id = models.CharField(max_length=50)  # Assuming dealer_id is a string, adjust as needed
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        # Add more choices as needed
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES)
    year = models.DateField()
    # Add any other fields you want for CarModel model

    def __str__(self):
        return f"{self.car_make.name} - {self.name}"


class CarDealer:
    def __init__(self, dealer_id, name, location):
        self.dealer_id = dealer_id
        self.name = name
        self.location = location


class DealerReview:
    def __init__(self, dealer_id, review_text, rating):
        self.dealer_id = dealer_id
        self.review_text = review_text
        self.rating = rating
