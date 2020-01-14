from django.db import models
import uuid
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(max_length=5000,blank=True)
    published = models.BooleanField()
    pub_date = models.DateField()
    video = models.ForeignKey('Video',on_delete=models.CASCADE, null=True , blank = True) 
    image = models.ForeignKey('Image',on_delete=models.CASCADE, null=True , blank = True)
    member = models.ManyToManyField('TeamMember')
    likes = models.DecimalField(default=0,max_digits=19, decimal_places=0)
    comments = models.ManyToManyField('Comment',blank=True,null=True)

    def __str__(self):
        return self.title

class Video(models.Model):   
    file = models.FileField(upload_to='videos/')

    def __str__(self):
        return str(self.file)

class Image(models.Model):
    file = models.ImageField(upload_to='img/')     

    def __str__(self):
        return str(self.file)

class TeamMember(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    role = models.ManyToManyField('MemberRole')
    
    def __str__(self):
        roles_str = ", ".join(str(r) for r in self.role.all())
        return str(self.user.get_username())+' | '+roles_str 

class MemberRole(models.Model):
    role = models.CharField(max_length=255)

    def __str__(self):
        return str(self.role)

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField(max_length=350,blank=False)

    def __str__(self):
        return str(self.user.get_username())+'->'+self.text