from django import forms

class ContactForm(forms.Form):
    full_name = forms.CharField()
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)


    def clean_email(self):
        email = self.cleaned_data.get('email')
        print(email)
        if email.endswith("abc"):
            raise forms.ValidationError("abc is not valid extension")
        return email
