from django.shortcuts import render

# Create your views here.
def example_view(request):
    # my_app/templates/my_app/example.html
    # render 내부의 폴더는 상기 주석의 후반부 의미함. 전반부는 프로젝트의 settings.py 에서 설정함
    return render(request, 'my_app/example.html')

def variable_view(request):
    my_var = {'first_name':'Rosaland', 'last_name':'Franklin', 
        'some_list':[1,2,3], 'some_dict':{'inside_key':'inside_value'}
    }
    return render(request, 'my_app/variable.html', context=my_var)
