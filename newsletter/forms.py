from django import forms

from .models import SignUp

class ContactForm(forms.Form):
    full_name=forms.CharField(required=False)
    email=forms.EmailField()
    message=forms.CharField()

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['full_name','email']
    def clean_email(self):
        email = self.cleaned_data.get('email')
    #     email_base,provider = email.split("@")
    #     domain,extention=provider.split(".")
    #     if not "@" in email:
    #         raise forms.ValidationError("Please provide an email id")
    #     if not extention == "com":
    #         raise forms.ValidationError("please provide a valid eamil_id")
        return email
    def clean_full_name(self):
        full_name=self.cleaned_data.get('full_name')
        #write the validation code here
        return full_name