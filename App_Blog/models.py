from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Blog(models.Model):
    # We use foreign key to stablish relation with User (name)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_author')
    blog_title = models.CharField(max_length=260, verbose_name='Title Here')
    # slag - when we open it in browser our url will be same as title
    slug = models.SlugField(max_length=264, unique=True)
    # verbose is place holder
    blog_content = models.TextField(verbose_name='Blog Content')
    blog_image = models.ImageField(upload_to='blog_images', verbose_name='Blog Image')
    # auto_now_add add time when blog is published and by setting True we can't change it
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    # to show field value in view
    def __str__(self):
        return self.blog_title



# it has relation with blog and user
class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment')
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-comment_date']
    def __str__(self):
        return self.comment


# For likes
class Likes(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_like')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_like')
