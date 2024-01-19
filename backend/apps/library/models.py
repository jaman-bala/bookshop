from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
	name = models.CharField(max_length=100)
	slug = models.SlugField(max_length=150, unique=True, db_index=True)
	icon = models.FileField(upload_to="category/")
	create_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = "Категорию"
		verbose_name_plural = "Категория"

	def __str__(self):
		return self.name


class Writer(models.Model):
	name = models.CharField(max_length=100)
	slug = models.SlugField(max_length=150, unique=True, db_index=True)
	bio = models.TextField()
	pic = models.FileField(upload_to="writer/", null=True, blank=True)
	create_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = "Авторов"
		verbose_name_plural = "Авторы"

	def __str__(self):
		return self.name


class Book(models.Model):
	writer = models.ForeignKey(Writer, on_delete=models.CASCADE)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100, db_index=True)

	coverpage = models.FileField(upload_to="coverpage/", null=True, blank=True)
	bookpage = models.FileField(upload_to="bookpage/", null=True, blank=True)

	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	description = models.TextField()
	video = models.FileField(upload_to="videos/", null=True, blank=True)
	pdf = models.FileField(upload_to="pdf/", null=True, blank=True)

	status = models.IntegerField(default=0)

	class Meta:
		verbose_name = "Книгу"
		verbose_name_plural = "Книги"

	def __str__(self):
		return self.name


class Review(models.Model):
	customer = models.ForeignKey(User, on_delete=models.CASCADE)
	book = models.ForeignKey(Book, on_delete=models.CASCADE)
	review_text = models.TextField()
	created = models.DateTimeField(auto_now_add=True)


class Slider(models.Model):
	title = models.CharField(max_length=150)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	slideimg = models.FileField(upload_to="slide/")

	def __str__(self):
		return self.title

