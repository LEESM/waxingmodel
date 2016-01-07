from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=2000)
    link = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    cafe_blog = models.CharField(max_length=200)

    def __str__(self):
    	return self.title