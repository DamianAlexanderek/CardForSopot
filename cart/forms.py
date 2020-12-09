from django import forms


class EmailPostForm(forms.Form):
    imie = forms.CharField(max_length=25)
    email = forms.EmailField()
    opis = forms.CharField(required=False,
                               widget=forms.Textarea)