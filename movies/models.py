from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length = 200)
    genre = models.CharField(max_length = 200)
    rating = models.CharField(max_length = 20)
    release_date = models.DateField(auto_now = False, auto_now_add = False)
    score = models.DecimalField(max_digits = 3, decimal_places = 1, blank = True, null = True)

    def __str__(self):
        return self.title
