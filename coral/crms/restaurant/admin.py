from django.contrib.sites.models import Site

from django.contrib import admin
from .models import (
    Food,
    Order,
    TableReservation,
    Reservation,
    Recreation,
    Activity,
)

# Register your models here.


admin.site.register(Food)
admin.site.register(Order)
admin.site.register(TableReservation)
admin.site.register(Reservation)
admin.site.register(Recreation)
admin.site.register(Activity)