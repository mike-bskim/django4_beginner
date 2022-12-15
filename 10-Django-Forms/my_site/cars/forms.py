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
        fields = '__all__' # ['first_name', 'last_name', 'stars']

        labels = {
            'first_name':'YOUR FIRST NAME',
            'last_name':'Last Name~~',
            'stars':'Rating',
        }

        # 사용자 전용 에러메시지 만드는 방법, 키-값을 쌍으로 추가.
        error_messages = {
            'stars':{
                'min_value':'Min value is 1',
                'max_value':'Max value is 5',
            },
        }
