from django.db import models
from django.contrib.auth.models import User
from napp.choices import *

class Author(models.Model):
	username = models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	designation = models.CharField(max_length=30, choices=DESIGNATION_CHOICE, default=1)
	avatar = models.ImageField(upload_to="pic_folder/", default="pic_folder/noimg.jpg")


class Notes(models.Model):
	author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='author')
	name = models.CharField(max_length=100)
	details = models.CharField(max_length=200)
	year = models.IntegerField(choices=YEAR_CHOICE)
	department = models.CharField(max_length=100, choices=DEPARTMENT_CHOICE)
	subject = models.CharField(max_length=100)
	unit = models.IntegerField()
	file = models.FileField(upload_to="notes_folder/")

	class Meta:
		verbose_name_plural = "Notes"

class Comment(models.Model):
	notes = models.ForeignKey('Notes', on_delete=models.CASCADE, related_name='notes') 
	comment = models.TextField(max_length=500)
	commented_by = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='commented_by')
	sentiment = models.CharField(max_length=20, choices=SENTIMENT_CHOICE)