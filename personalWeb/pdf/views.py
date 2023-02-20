from django.shortcuts import render

# Create your views here.
def pdf(request):
    # Only assigns project with the 5 most recent post


    return render(request, 'pdf/home.html')
