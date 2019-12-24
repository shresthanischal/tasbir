from django import forms
from .models import PostModel

class AddNewPostFrom(forms.ModelForm):

    class Meta:
        model = PostModel
        fields ={
            'location',
            'photo',
        }