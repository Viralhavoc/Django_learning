from django.shortcuts import render

def page_1_view(request):
    return render(request, 'my_app/page_1.html', {})