from django.shortcuts import render, HttpResponse
from datetime import datetime

# Create your views here.
def show_hello(request):
    return HttpResponse("Hello World!")

def show_html(request):

    context = {
        'mainigais': 'kaut ko',
        'cits': 42
    }
    
    return render(request, template_name='index.html', context=context)


def get_time(request):
    time = datetime.now()
    context = {
        'time': time,
    }
    time = datetime.now()
    return render(request, template_name='time.html', context=context)

def enter_name(request):

    if request.method == 'POST':
        name = request.POST['name']
        return HttpResponse(name)

    return render(request,
                  template_name='forma.html')

