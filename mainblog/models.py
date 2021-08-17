from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.utils.text import slugify

class Post(models.Model):
    title = models.CharField(max_length=150, verbose_name='Title')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='author')
    descr = models.CharField(max_length=200, verbose_name='Description')
    body = models.TextField(verbose_name='Post Body')
    pub_date = models.DateTimeField(auto_now_add=True)
    post_type = models.TextChoices('post_type','Food Travel Lifestyle Fashion')
    category = models.CharField(max_length=20, choices=post_type.choices, default='Food')
    slug = models.SlugField(default="my-post-name", max_length=200)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

class Comment(models.Model):
    message = models.TextField()
    email = models.EmailField(blank=True)
    username = models.CharField(max_length=100, default="anonymous")
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.message

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['message', 'email', 'username']

class Category(models.Model):
    name = models.CharField(max_length = 20, verbose_name="category_name")
