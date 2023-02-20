from django.contrib import admin

# Register your models here.
from .models import Project, Publication, Skill, ContactForm, ML, Cert
admin.site.register(Project)
admin.site.register(Publication)
admin.site.register(Skill)
admin.site.register(ContactForm)
admin.site.register(ML)
admin.site.register(Cert)