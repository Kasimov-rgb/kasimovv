from django import forms

from apps.fasts.models import Fast, Images


class ImagesForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ('image', )
        widgets = {'image': forms.ClearableFileInput(attrs={
            'class': 'form-control-file'
        })}


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Fast
        fields = ('description', 'location', 'tags')
