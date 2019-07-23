from django import forms

from contact.models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['email', 'subject', 'text']
