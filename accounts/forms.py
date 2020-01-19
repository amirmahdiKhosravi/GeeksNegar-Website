from django import forms
    
class ProfilePicForm(forms.Form):
    pic = forms.FileField(label="Profile Picture")
