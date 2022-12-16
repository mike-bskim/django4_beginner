from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from classroom.forms import ContactForm

# Create your views here.
# def home_view(request):
#     return render(request, 'classroom/home.html')

class HomeView(TemplateView):
    template_name = 'classroom/home.html'

class ThankYouView(TemplateView):
    template_name = 'classroom/thank_you.html'
    
class ContactFormView(FormView): # <=== 추가 부분
    # 1. 폼 클래스 연결, 
    form_class = ContactForm # 인스턴스 생성하기전에 연결만 함.
    # 2. 폼과 연결할 template_name 설정
    template_name = 'classroom/contact.html' 

    # 3. 정상일때 이동할 URL 설정.
    # success URL?, URL is not a template.html
    success_url = '/classroom/thank_you/' 
    # 여기서 reverse 를 사용하고 싶다면 reverse_lazy() 를 사용해야 한다(lazy는 object 리턴). 외울것.
    # success_url = reverse_lazy('classroom:thank_you')

    # what to do with form?
    def form_valid(self, form):
        print(form.cleaned_data)
        # ContactForm(reques.POST)
        return super().form_valid(form)