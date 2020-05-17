from django.contrib import admin

# Register your models here.

from .models import Post, Employee

class PostAdmin(admin.ModelAdmin):
    list_display = ["__str__", "dateTimeStamp"]
    list_filter = ["messageId", "dateTimeStamp"]
    search_fields = ["message", "messageId"]
    class Meta:
        model = Post


admin.site.register(Post, PostAdmin)
admin.site.register(Employee)