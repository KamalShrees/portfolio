import email
from django import forms
from .models import Contact
from django.core.validators import RegexValidator

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class']="form-control"
        self.fields['name'].widget.attrs['placeholder']="Name"
        
        self.fields['email'].widget.attrs['class']="form-control"
        self.fields['email'].widget.attrs['placeholder']="Email"
        
        self.fields['subject'].widget.attrs['class']="form-control"
        self.fields['subject'].widget.attrs['placeholder']="Subject"
        
        self.fields['message'].widget.attrs['class']="form-control"
        self.fields['message'].widget.attrs['placeholder']="Type Your Message ......."
    
    def clean_name(self):
        string_validate = RegexValidator(r'^(([A-Za-z]+)(\s[A-Za-z]+)?)$')
        name = self.cleaned_data.get('name')
        if name == string_validate:
            msg = 'Only alphabet are allowed'
            self.add_error('name', msg)
        return name
        
    def clean_subject(self):
      subject = self.cleaned_data['subject']
      if len(subject)>10:
        msg = 'subject is too long'
        self.add_error('subject', msg)

      return subject