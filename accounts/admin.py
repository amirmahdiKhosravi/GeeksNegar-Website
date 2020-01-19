from django.contrib import admin
from blog.models import CustomUser
from django.utils.safestring import mark_safe


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id','user','profile_pic','image_thumb')
    fields = ( 'user','image_show', )
    readonly_fields = ('image_show',)
    def image_show(self,obj):
        if not obj.file:
            return 'Please upload the image to show preview'
        return mark_safe('<img src="%s" width=\'300\' height=\'300\'/>' % str('/media/'+str(obj.profile_pic)))
    image_show.allow_tags = True
    image_show.__name__ = 'Image View'
    def image_thumb(self,obj):
        return mark_safe('<img src="%s" width=\'100\' height=\'100\'/>' % str('/media/'+str(obj.profile_pic)))
    image_show.allow_tags = True
    image_show.__name__ = 'Preview'
