from django.shortcuts import render


# Create your views here.
def jinja_print(request):
    d={'name':'kavitha','age':22}
    return render(request, 'jinja.html',d)