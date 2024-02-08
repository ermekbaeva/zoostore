from django.shortcuts import render

def index(request):
    context={
        'title':'Home',
        'content':'Main page'
    }
    return render(request, 'main/index.html', context)
