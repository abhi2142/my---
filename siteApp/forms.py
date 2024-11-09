from django import forms
from .models import ContactForm, NewsletterSubscription

class ContactFormModel(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['full_name', 'email', 'mobile_number', 'city']


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscription
        fields = ['email']