from django import forms

class ProfilePicForm(forms.Form):
    pic = forms.ImageField()

class AddPostForm(forms.Form):
    title = forms.CharField()
    caption = forms.CharField()
