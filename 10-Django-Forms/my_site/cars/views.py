from django.shortcuts import render, redirect
from django.urls import reverse
from . import forms

# Create your views here.
def rental_review(request):
    # POST REQEUEST --> Form Contents --> Thank you
    if request.method == 'POST':
        form = forms.ReviewForm(request.POST)
        if form.is_valid():
            # {'first_name':'Jose', 'last_name' , 'email' ~~~~}
            print(form.cleaned_data)
            form.save() # 모델로 전달된 내용을 자동 저장
            return redirect(reverse('cars:thank_you'))
        else:
            print('~~~is not valid')
            print(form.cleaned_data)

    else:
        form = forms.ReviewForm()
    # return render(request, 'cars/rental_review.html')
    return render(request, 'cars/rental_review.html', context={'form':form})

def thank_you(request):
    return render(request, 'cars/thank_you.html')    