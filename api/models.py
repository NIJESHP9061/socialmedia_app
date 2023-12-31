from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count

# Create your models here.
class Posts(models.Model):
    title=models.CharField(max_length=250)
    image=models.ImageField(upload_to="images",null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateField(auto_now_add=True)
    like=models.ManyToManyField(User,related_name="likes")

    @property
    def posts_comments(self):
        return self.comments_set.all()

    @property
    def likes(self):
        qs=self.like.all().count()
        return qs

    def _str_(self):
        return self.title

class Comments(models.Model):
    comment=models.CharField(max_length=250)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Posts,on_delete=models.CASCADE)
    created_date=models.DateField(auto_now_add=True)

    def _str_(self):
        return self.comment


class Userprofile(models.Model): 
    user=models.OneToOneField(User,on_delete=models.CASCADE,) 
    proimage=models.ImageField(upload_to="images",null=True) 
    timelinepic=models.ImageField(upload_to="timelinepic",null=True) 
    followings=models.ManyToManyField(User,related_name="following")

class Friends(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    date = models.DateTimeField(auto_now_add=True)