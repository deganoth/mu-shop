from django import forms
from django.forms import ModelForm, Textarea, NumberInput
from .models import Review


class ReviewForm(forms.ModelForm):

    class Meta:

        model = Review
        fields = ('rating', 'comment')
        widgets = {'comment': Textarea(attrs={'id': 'comment',
                   'type': 'text', 'class': 'materialize-textarea'}),
                   'rating': NumberInput(
                       attrs={
                            'id': 'rating',
                            'type': 'number',
                            'min': 1,
                            'max': 5,
                            'class': 'validate',
                            }
                        )
                   }
