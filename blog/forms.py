from django import forms
    
class CommentForm(forms.Form):
    comment_text = forms.CharField(label="Your Comment",widget=forms.Textarea(attrs={'class' : 'form-control'}))

