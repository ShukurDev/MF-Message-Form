from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Contact
# Create your views here.
def index(request):
    return render(request , 'home.html')

class ContactFormView(CreateView):
    model = Contact
    template_name = 'contactform.html'
    fields = ('name'  ,'email' ,'phone' , 'subject' ,'message')