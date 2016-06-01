from django.db import models

class Day(models.Model):
    day_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.day_name

class Food(models.Model):
    food_time = models.CharField(max_length=100)
    day = models.ForeignKey(Day)
    
    def __str__(self):
        return self.food_time
