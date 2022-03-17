from django.contrib.auth.forms import UserCreationForm
from django import forms

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)


class SearchForm(forms.Form):
    search = forms.CharField(label="Search", max_length=100)
    # class Meta:
    #     fields = ("search",)