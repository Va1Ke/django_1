from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields=['title','shortdiscription','full_text','date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Topic of an article'
            }),
            'shortdiscription': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Anons of an article'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Time of publishing'
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Text of an article'
            })
        }