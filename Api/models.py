from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=150)
    def __str__(self):
        return self.title

class Post(models.Model):
    
    user=models.ForeignKey(User,models.CASCADE)
    title=models.CharField(max_length=150)
    category=models.ForeignKey(Category,models.CASCADE)
    code=models.TextField()
    content=models.TextField() 
    date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title

class Comment(models.Model):
    user=models.ForeignKey(User,models.CASCADE)
    post=models.ForeignKey(Post,models.CASCADE)
    title=models.TextField()
    time=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title
    

class Reply(models.Model):
    user=models.ForeignKey(User,on_delete= models.CASCADE)
    comment=models.ForeignKey(Comment,on_delete= models.CASCADE)
    title=models.TextField()
    time=models.DateField(auto_now_add=True)
    def __str__(self):
        return f"user={self.user.username}||comment={self.comment}"

class Likes(models.Model):
    user=models.ForeignKey(User,models.CASCADE)
    post=models.ForeignKey(Post,models.CASCADE)
    like=models.BooleanField(default=False)
    time=models.DateField(auto_now_add=True)
    def __str__(self):
        return f"Post={self.post.id}||user={self.user.username}||Likes={self.like}"

# class ImageGet(models.Model):
#     Image=models.ImageField(default='default.jpg', upload_to='profile_pics')

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Delete profile when user is deleted
    image = models.CharField( max_length=500)

    def __str__(self):
        return f'{self.user.username} Profile'
    

    




