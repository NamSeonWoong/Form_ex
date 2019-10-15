from django import forms
from .models import Movie

class MovieModelForm(forms.ModelsForm):
    open_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    class Meta:
        model = Movie
        fields = '__all__'