from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id','file','image_thumb')
    fields = ( 'file','image_show', )
    readonly_fields = ('image_show',)
    def image_show(self,obj):
        if not obj.file:
            return 'Please upload the image to show preview'
        return mark_safe('<img src="%s" width=\'300\' height=\'300\'/>' % str('/media/'+str(obj.file)))
    image_show.allow_tags = True
    image_show.__name__ = 'Image View'
    def image_thumb(self,obj):
        return mark_safe('<img src="%s" width=\'100\' height=\'100\'/>' % str('/media/'+str(obj.file)))
    image_show.allow_tags = True
    image_show.__name__ = 'Preview'

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('id','file','video_thumb')
    fields = ( 'file','video_show', )
    readonly_fields = ('video_show',)
    def video_show(self,obj):
        if not obj.file:
            return 'Please upload the video to show preview'
        return mark_safe('<video width="800" height="450" controls><source src="%s" type="video/mp4"></video>' % str('/media/'+str(obj.file)))
    video_show.allow_tags = True
    video_show.__name__ = 'video View'
    def video_thumb(self,obj):
        return mark_safe('<video width="160" height="90" autoplay><source src="%s" type="video/mp4"></video>' % str('/media/'+str(obj.file)))
    video_show.allow_tags = True
    video_show.__name__ = 'Preview'

@admin.register(MemberRole)
class MemberRoleAdmin(admin.ModelAdmin):
    list_display = ('id','role')

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    pass

class TeamMemberInline(admin.TabularInline):
    model = TeamMember
    extra = 2

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = ('title', 'text','pub_date')
    list_display = ('id','title', 'published', 'get_members')
    def get_members(self, obj):
        return " | ".join([p.user.get_username() for p in obj.member.all()])
    get_members.short_description = 'member(s)'
    #readonly_fields=('likes', )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','user','text')

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('id','get_users','post','likecount')

    def get_users(self, obj):
        return " | ".join([p.get_username() for p in obj.user.all()])
@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display=('id', 'header')
