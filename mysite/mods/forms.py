from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from .models import Mod, Discussion, Reply

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)


class SearchForm(forms.Form):
    search = forms.CharField(label="Search", max_length=100)
    # class Meta:
    #     fields = ("search",)


class PublishForm(ModelForm):
    class Meta:
        model = Mod
        fields = ['mod_title', 'mod_author', 'mod_game', 'mod_source', 'mod_description']


class DiscussionForm(ModelForm):
    class Meta:
        model = Discussion
        fields = ['dis_title', 'dis_author', 'dis_type', 'dis']


class ReplyForm(ModelForm):
    class Meta:
        model = Reply
        fields = ['rep_parent','rep_title', 'rep_author', 'rep']
