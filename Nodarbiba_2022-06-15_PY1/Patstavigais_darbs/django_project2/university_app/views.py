from django.shortcuts import render, HttpResponse

# Create your views here.
def enter_data(request):

    if request.method == 'POST':
        name = request.POST['name']
        math_grade = request.POST['math_grade']
        lat_lan_grade = request.POST['lat_lan_grade']
        for_lan_grade = request.POST['for_lan_grade']
        if (int(math_grade) < 40) or (int(lat_lan_grade) < 40) or (int(for_lan_grade) < 40):
            response = name + " can not apply to university"
            return HttpResponse(response)
        else:
            response = name + " welcome to university"
            return HttpResponse(response)    

    return render(request,
                  template_name='forma.html')