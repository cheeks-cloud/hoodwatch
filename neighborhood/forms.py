from django import forms
from neighborhood.models import *


class CreateBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = [
            'business_name',
            'email'
        ]


class HoodCreationForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        fields = [
            'hood_name',
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