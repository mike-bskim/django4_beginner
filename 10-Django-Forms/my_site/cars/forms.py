from django import forms

class ReviewForm(forms.Form):
    first_name = forms.CharField(label = 'First Name', max_length=100)
    last_name = forms.CharField(label = 'Last Name', max_length=100)
    email = forms.CharField(label = 'Email', max_length=100, required=False)
    review = forms.CharField(label='Please write your review here', required=False)

    