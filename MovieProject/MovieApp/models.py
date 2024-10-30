from django.db import models
#from django.db import forms
#Create your models here.
class Movies(models.Model):
    releasedate=models.DateField()
    moviename=models.CharField(max_length=30)
    actor=models.CharField(max_length=30)
    actress=models.CharField(max_length=30)
    rating=models.FloatField()

# class MoviesForm(forms.ModelForm):
#     releasedate = forms.DateField(widget=DateInput())
#     moviename = forms.CharField()
#     actor = forms.CharField()
#     actress = forms.CharField()
#     rating = forms.FloatField()
#     class Meta:
#         model = Movies
#         fields = ('releasedate','moviename', 'actor', 'actress', 'rating');
