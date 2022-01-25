from django.contrib import admin
from .models import Payment

# Register your models here.

class show(admin.ModelAdmin):
     list_display=("verified","email","amount","ref","date_created",)
     list_filter=("email",)

admin.site.register(Payment, show)