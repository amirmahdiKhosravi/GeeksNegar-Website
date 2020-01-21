from django.db import models
import uuid
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(max_length=5000,blank=True)
    published = models.BooleanField()
    pub_date = models.DateField()
    video = models.ForeignKey('Video',on_delete=models.SET_NULL, null=True , blank = True)
    image = models.ForeignKey('Image',on_delete=models.SET_NULL , null=True , blank = True)
    member = models.ManyToManyField('TeamMember')
    #likes = models.ManyToManyField('Like',blank=True,null=True)
    comments = models.ManyToManyField('Comment',blank=True,null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('blog:post-detail',args=[str(self.id)])

class CustumPost(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular post")
    user=models.ForeignKey(User, on_delete=models.PROTECT, null=True , blank = False)
    title = models.CharField(max_length=255)
    text = models.TextField(max_length=300,blank=True)

    def __str__(self):
        return self.title

class CustomUser(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pic=models.ImageField(upload_to='img/profilepics/',default='img/profilepics/default-avatar.png')

class Video(models.Model):
    file = models.FileField(upload_to='videos/')

    def __str__(self):
        return str(self.file)

class Image(models.Model):
    file = models.ImageField(upload_to='img/')

    def __str__(self):
        return str(self.file)

class Slider(models.Model):
    image= models.ForeignKey('Image',on_delete=models.CASCADE, null=False, blank=False )
    header= models.CharField(max_length=50, null=False, blank=False)
    caption=models.CharField(max_length=70, null=True, blank=True)

class TeamMember(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    role = models.ManyToManyField('MemberRole')

    def __str__(self):
        roles_str = ", ".join(str(r) for r in self.role.all())
        return str(self.user.user.get_username())+' | '+roles_str

class MemberRole(models.Model):
    role = models.CharField(max_length=255)

    def __str__(self):
        return str(self.role)

class Comment(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    text = models.TextField(max_length=350,blank=False)

    def __str__(self):
        return str(self.user.user.get_username())+'->'+self.text

class Like(models.Model):
    user = models.ManyToManyField(User, related_name='likes',null=True)
    post = models.ForeignKey(Post, on_delete=models.SET_NULL,null=True)
    likecount = models.IntegerField(default=0)

    def __str___(self):
        return str(self.user.get_username())
