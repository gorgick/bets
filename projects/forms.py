from projects.models import Project
from django import forms


class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ("name", "description", "price", "image", "creator")

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'cols': '4', 'rows': '4'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'required': False, }),
            'creator': forms.Select(attrs={'class': 'form-control', 'default': 'self.request.user'}),
        }