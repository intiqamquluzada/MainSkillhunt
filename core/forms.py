from django import forms

from core.models import JobPost, Candidates, ContactModel


class JobPostForm(forms.ModelForm):
    CHOICES = (
        ('full_time', 'Full time'),
        ('part_time', 'Part time'),
        ('freelance', 'Freelance'),
        ('internship', 'Internship'),
        ('termporary', 'Termporary')
    )

    job_type = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = JobPost
        fields = ['title', 'company', 'location', 'description', 'job_type']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'company': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5})
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your subject'}),
            'message': forms.Textarea(
                attrs={'class': 'form-control', 'cols': 30, 'rows': 7, 'placeholder': 'Your message'})
        }
