from __future__ import unicode_literals
from django.db import models

class MovieManager(models.Manager):
    def addMovie(self, title, year):
        print title, year
        errors = []
        if len(title) == 0:
            errors.append('Title is required')
        if year > 2025:
            errors.append("year is too far in the future")
        elif year < 1900: 
            errors.append('year is so 19th century')
        
        if len(errors) > 0: 
            return errors 
        else: 
            return Movie.objects.create(title=title, year=year)
        

class Movie(models.Model): #inherit from models.Model need very little code to make it work. base class for table in database
    title = models.CharField(max_length=255) 
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    objects = MovieManager()

class Actor(models.Model): #inherit from models.Model need very little code to make it work. base class for table in database
    name = models.CharField(max_length=255) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

class Cast(models.Model): #refers to only the movie and actors tables 
    movie = models.ForeignKey(Movie, related_name="actors") # can use the related name to call this key 
    actor = models.ForeignKey(Actor, related_name="movies")
