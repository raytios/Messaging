from django.contrib import admin

# Register your models here.

from .models import Collaborate_Messaging_A00

class Collaborate_Messaging_A00_Admin(admin.ModelAdmin):
    list_display = ["__str__", "dateTimeStamp"]
    list_filter = ["Collaborate_Messaging_A00_Rec", "dateTimeStamp"]
    search_fields = ["message", "Collaborate_Messaging_A00_Rec"]
    class Meta:
        model = Collaborate_Messaging_A00


admin.site.register(Collaborate_Messaging_A00, Collaborate_Messaging_A00_Admin)
#admin.site.register(Employee)