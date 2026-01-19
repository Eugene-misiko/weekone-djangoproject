from django.db import models
from django.utils import timezone
# Create your models here.
class FoodItem(models.Model):
    """
    Represents a food item consumed by the user.
    """
    name = models.CharField(max_length=100)
    carlories = models.PositiveIntegerField()
    date_added = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.name} - {self.carlories} kcal"