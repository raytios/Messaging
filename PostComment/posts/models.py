from django.db import models
from django.contrib.auth.models import Permission, User
from django.urls import reverse

# Create your models here.

class Collaborate_Messaging_A00(models.Model):

    Collaborate_Messaging_A00_Rec = models.AutoField(primary_key=True)
    POST ='POST'
    REPLY='REPLY'
    MESSAGE_TYPE_CHOICES = [
        (POST, 'Post'),
        (REPLY, 'Reply'),

    ]
    messageType = models.CharField(max_length=10, choices= MESSAGE_TYPE_CHOICES, default=POST, db_column='Message_Type')
    parentPostId = models.ForeignKey('posts.Collaborate_Messaging_A00', on_delete=models.SET_NULL, null=True, blank=True)
    message = models.TextField()
    dateTimeStamp = models.DateTimeField(auto_now=True, auto_created=True)

    def __str__(self):
        return 'Collaborate_Messaging_A00_Rec' + str(self.Collaborate_Messaging_A00_Rec)

    def get_absolute_url(self):
        return reverse("detail", kwargs={"Collaborate_Messaging_A00_Rec": self.Collaborate_Messaging_A00_Rec})

"""
class Employee(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE,)
    employee_no = models.IntegerField()
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)


    def __str__(self):
        return self.first_name + '   ' + self.last_name

"""








