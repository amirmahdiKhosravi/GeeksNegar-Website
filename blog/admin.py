from django.contrib import admin
from .models import Image, MemberRole, Post, TeamMember, Video, Comment

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    pass

@admin.register(MemberRole)
class MemberRoleAdmin(admin.ModelAdmin):
    pass

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
    readonly_fields=('likes', )

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass