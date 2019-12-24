from django import forms
from .models import UserModel

class EditProfileForm(forms.ModelForm):
    display_name = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                'class' : 'edit-profile__input',
            }
        )
    )

    username = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                'class' : 'edit-profile__input',
            }
        )
    )

    bio = forms.CharField(
        widget = forms.Textarea(
            attrs = {
                'class' : 'edit-profile__input',
            }
        )
    )

    email = forms.EmailField(
        widget = forms.TextInput(
            attrs = {
                'class' : 'edit-profile__input',
            }
        )
    )

    class Meta:
        model = UserModel
        fields ={
            'display_name',
            'username',
            'bio',
            'profile_pic',
            'email',
        }