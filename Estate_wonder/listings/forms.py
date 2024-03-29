from django import forms
from .models import Listing

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'price', 'bedrooms', 'bathrooms', 'sqft', 'photo_main', 'photo_1', 'photo_2', 'photo_3', 'is_published']
