from django.shortcuts import render, HttpResponse, redirect
from .forms import ContactFormModel, SubscribeForm
from .models import Project, Client

def submitMail(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        
        if form.is_valid():
            form.save()
    return redirect('land')


def landing_page(request):
    form_submitted = False  # To track whether the form is submitted or not
    project = Project.objects.all()
    client = Client.objects.all()
    data = {
        'projects': project,
        'clients': client,
    }
    
    if request.method == 'POST':
        form = ContactFormModel(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            form_submitted = True  # Set the flag to True to show the thank you message
    else:
        form = ContactFormModel()
        
    data['form'] = form
    data['form_submitted'] = form_submitted
    data['subForm'] = SubscribeForm
    return render(request, 'base.html', data)
