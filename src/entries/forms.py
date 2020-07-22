from django import forms
from .models import Entry

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = [
            'item',
            'cost'
        ]
        widgets = {
            'item': forms.TextInput(
				attrs={
					'class': 'form-control'
					}
				),
            'cost': forms.TextInput(
				attrs={
					'class': 'form-control'
					}
				),
			}