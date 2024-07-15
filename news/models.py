from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User(User):
    pass

class Author(models.Model):
    author_name = models.CharField(max_length=30)

    def __str__(self):
        return self.author_name

class Category(models.Model):
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name

class Articles(models.Model):
    title = models.CharField(max_length=70)
    short_description = models.CharField(max_length=300,default="hello")
    description = models.CharField(max_length=2000)
    tags = models.CharField(max_length=20)
    imageUrl = models.CharField(max_length=1000)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,blank=True,null=True,related_name="author")
    category = models.ForeignKey(Category, on_delete=models.CASCADE,blank=True,null=True,related_name="category")
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comments(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE,blank=True,null=True,related_name="author_comments")
    article = models.ForeignKey(Articles, on_delete=models.CASCADE,blank=True,null=True,related_name="article_comment")
    message = models.CharField(max_length=300)
    name = models.CharField(max_length=50,default="hey")

    def __str__(self):
        return f"{self.author} comment on {self.article}"


