from django.db import models
import uuid
from django.contrib.auth.models import User

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular post")
    title = models.CharField(max_length=255)
    text = models.TextField(max_length=255,blank=True)
    published = models.BooleanField()
    pub_date = models.DateField()
    video = models.ForeignKey('Video',on_delete=models.CASCADE, null=True , blank = True) 
    image = models.ForeignKey('Image',on_delete=models.CASCADE, null=True , blank = True)
    member = models.ManyToManyField('TeamMember')

    def __str__(self):
        return self.title

class Video(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular video")    
    file = models.FileField(upload_to='videos/')

    def __str__(self):
        return str(self.file)

class Image(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular img")  
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
