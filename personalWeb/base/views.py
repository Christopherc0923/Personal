from django.shortcuts import render
from .models import Project, Publication, Skill, ContactForm, ML, Cert


# Create your views here.
def home(request):
    projects = Project.objects.all()
    skills = Skill.objects.all().order_by('title')
    context = {'projects': projects, 'skills': skills}
    return render(request, 'base/home.html', context)

def publication(request):
    publications = Publication.objects.all()
    context = {'publications': publications}
    return render(request, 'base/publication.html', context)

def contact(request):
    return render(request, 'base/contact.html')

def resume(request):
    return render(request, 'base/resume.html')

def ibm(request):
    return render(request, 'base/IBMppt.html')

def eid101(request):
    return render(request, 'base/eid101.html')

def cert(request):
    certs = Cert.objects.all()
    context = {'certs': certs}
    return render(request, 'base/cert.html', context)

def landing(request):
    return render(request, 'base/landing.html')

# Admin
from django.urls import reverse
from django.shortcuts import redirect

def adminPage(request):
    admin_url = reverse('admin:index')
    return redirect(admin_url)

def mlproj(request):
    MLs = ML.objects.all()
    context = {'MLs': MLs}
    return render(request, 'base/mlproj.html', context)

def contact_submit(request):
    if request.method == 'POST':
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        find = request.POST.get('find')
        info = request.POST.get('textBox')
        file = request.FILES.get('file')
        term = request.POST.get('term') == "on"

        contact_form = ContactForm(
        first_name=first_name,
        last_name=last_name,
        email=email,
        phone_number=phone,
        find=find,
        additional_info=info,
        file=file,
        terms=term
        )

        contact_form.save()

        # Do something with the form data, such as sending an email or saving it to the database
        
        # Redirect to a success page
        return render(request, 'base/contact_submit.html')

    # If the request is not a POST, return the form template
    return render(request, 'base/contact.html')