from django import forms
from neighborhood.models import *


class CreateBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = [
            'name',
            'email'
        ]


class HoodCreationForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        fields = [
            'name',
            'location'
        ]


class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'image',
            'content'
        ]