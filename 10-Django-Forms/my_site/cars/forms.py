from django import forms
from .models import Review
from django.forms import ModelForm

# class ReviewForm(forms.Form):
#     first_name = forms.CharField(label = 'First Name', max_length=100)
#     last_name = forms.CharField(label = 'Last Name', max_length=100)
#     email = forms.CharField(label = 'Email', max_length=100, required=False)
#     review = forms.CharField(label='Please write your review here', required=False, 
#                              widget=forms.Textarea(attrs={'class':'myform', 'rows':'2', 'cols':'2'}))


# https://docs.djangoproject.com/en/4.1/topics/forms/modelforms/
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['first_name', 'last_name', 'stars']
