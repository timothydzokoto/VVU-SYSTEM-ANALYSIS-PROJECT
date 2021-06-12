from django.forms import  ModelForm
from .models import TableReservation, Recreation


class TableReservationForm(ModelForm):
    class Meta:
        model = TableReservation
        fields = ('type', 'no_people', 'phone', 'comment')

class RecreationForm(ModelForm):
    class Meta:
        model = Recreation
        fields = ('activity', 'no_days', 'phone', 'comment')
        
