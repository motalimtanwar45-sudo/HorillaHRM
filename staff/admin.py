from django.contrib import admin
from .models import Employee

# सिर्फ Employee को रजिस्टर कर रहे हैं
admin.site.register(Employee)