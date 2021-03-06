from django.contrib import admin
from .models import Movie, Celebrity #importing our models

class MoviesInline(admin.TabularInline):
    model = Movie
    extra = 1 #for now its 1 because I don't have many movies added


class MovieAdmin(admin.ModelAdmin): #making a MovieAdmin class so we can pass it when registering a model
    #fieldsets configures the way we view the options when creating a new model (it splits them into sections like 'General Information' or 'Other', etc.)
    fieldsets = [
        (None, {'fields': ['title']}), #there will be no section because this is our 'main' field (personal preference)
        ('General Information', {'fields': ['genre','rating','duration','release_date']}), #grouping all the general info fields
        ('Other', {'fields': ['description']}), #same thing is applied here
        ('Celebrities', {'fields': ['director']}),
    ]
    list_display = ('title','genre','rating','release_date','duration') #list_display determines the models' fields we see when we view all the models we have created
    list_filter = ['genre','rating'] #using list_filter we can filter by any criteria we want (here we can filter the movies by 'genre' and 'rating') 
    search_fields = ['title','genre','release_date','director'] #using search_fields we can search for models based on some of their fields

class CelebrityAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Personal Info',{'fields': ['first_name','last_name','age','job']}),
        ('Carrer Highlights', {'fields': ['career_highlight']}),
    ]
    inlines = [MoviesInline]
    list_display = ('first_name','last_name','age','job')
    list_filter = ['job']
    search_fields = ['first_name','last_name','job']   

#this is how we register our models so we can work with them using the admin interface django provides 
admin.site.register(Movie, MovieAdmin) #passing the MovieAdmin that was created earlier so we have more control and better interaction with the models we created
admin.site.register(Celebrity, CelebrityAdmin)

