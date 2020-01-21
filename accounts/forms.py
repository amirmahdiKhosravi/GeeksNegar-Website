from django import forms

class ProfilePicForm(forms.Form):
    pic = forms.ImageField()

class AddPostForm(forms.Form):
    title = forms.CharField(label="Title:",widget=forms.TextInput(attrs={'class' : 'form-control'}))
    caption = forms.CharField(label="Caption:",widget=forms.Textarea(attrs={'class' : 'form-control'}))
