from django.shortcuts import render

# Create your views here.
def expense(request):
    return render(request, 'expense/home.html')
