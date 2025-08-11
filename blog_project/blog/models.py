from django.db import models
from django.contrib.auth.models import User
#Imports the built-in User model Django provides for authentication.
# You’ll use this to link posts and comments to registered users.
from django.utils.text import slugify
#slug → URL-identifier
#slugify → URL-convert
#Models as given below:
class Category(models.Model):
    name=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(unique=True,blank=True)
    def save(self,*args,**kwargs):#Overrides .save() so the slug auto-generates from the category name only if not already set.
        if not self.slug:
            self.slug=slugify(self.name)
        super().save(*args,**kwargs)
    def __str__(self):#Makes admin/console display show the name instead of "Category object(1)".
        return self.name    
class Post(models.Model):
    STATUS_CHOICES=(('draft','Draft'),('published','Published'),)
    #Dropdown choices for post status.
    title=models.CharField(max_length=100)
    slug=models.SlugField(unique=True,blank=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True)
    content=models.TextField(max_length=10000)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    '''
title → Post title.

slug → URL slug (auto-generated from title in save).

author → Link to the User who wrote it. on_delete=models.CASCADE means if the user is deleted, their posts go too.

category → Optional link to a Category. If category is deleted, it’s set to NULL instead of deleting the post.

content → Main article text.

status → "draft" or "published".

created_at → Auto-filled when first created.

updated_at → Auto-updated on every save.
    '''
    def save(self,*args,**kwargs):#Auto-creates slug from title if not set.
        if not self.slug:
            self.slug=slugify(self.name)
        super().save(*args,**kwargs)
    def __str__(self):#Shows the title in admin/console.
        return self.title
class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.TextField(max_length=1000)
    created_at=models.DateTimeField(auto_now_add=True)
    '''
    post → Which post this comment belongs to.

related_name="comments" means you can do post.comments.all() in code to get all comments for a post.

author → Which user wrote the comment.

content → Comment text.

created_at → Auto-set when comment is created.
    '''
    def __str__(self):
        return f"Comment by {self.author} on{self.post}"       
