from django.db import models


# Create your models here.
class Author(models.Model):
	firstname=models.CharField(max_length=20)
	lastname=models.CharField(max_length=20)
	dateofbirth=models.DateField(null=True)
	dateofdeath=models.DateField(null=True,blank=True)

	def __str__(self):
		return self.firstname

class Genre(models.Model):
	name=models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Language(models.Model):
	lname=models.CharField(max_length=100)

	def __str__(self):
		return self.lname

class Book(models.Model):
	title=models.CharField(max_length=40)
	author=models.ForeignKey('Author',on_delete=models.CASCADE)
	summary=models.TextField()
	genre=models.ManyToManyField('Genre')
	language=models.ManyToManyField('Language')

	def __str__(self):
		return self.title