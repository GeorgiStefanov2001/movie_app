from django.db import models

#this is how we create a model
class Movie(models.Model):
    #inside this class we create all the fields we want our model to have

    #CharField is for smaller text and 'max_length' is a required argument
    title = models.CharField(max_length = 140) 
    genre = models.CharField(max_length = 100) 
    rating = models.CharField(max_length = 20)

    #TextField is for bigger texts
    description = models.TextField(null = True)

    #we set auto_now to False because we don't want the movie's release date to be the current date 
    #and vice versa for auto_now_add (when adding a new model) 
    release_date = models.DateField(auto_now = False, auto_now_add = False)

    #decimal_places = 1 means that all numbers will be formated like so '7.0' or '5.4', etc.
    #max_digits takes decimal_places into account
    #so having max_digits = 3 and decimal_places = 1 we can have a a maximum number of '10.0'
    score = models.DecimalField(max_digits = 3, decimal_places = 1, null = True)
    
    def __str__(self):
        return self.title
