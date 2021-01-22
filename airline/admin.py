from django.contrib import admin
from .models import flights,airport,passenger
# Register your models here.
admin.site.register(flights)
admin.site.register(airport)
admin.site.register(passenger)
