
from django.core.files.base import ContentFile
from django import forms
from .models import Image


class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'image', 'description')


    def save(self, force_insert=False, force_update=False, commit=True):
        image = super(ImageCreateForm, self).save(commit=False)
        image_name = '{}'.format(image.title)
        image.image.save(image_name,
                         ContentFile('image'),
                         save=False)

        if commit:
            image.save()
        return image