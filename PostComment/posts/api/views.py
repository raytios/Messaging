from rest_framework import generics
from posts.models import Collaborate_Messaging_A00
from .serializers import FUMSerializer,  MessageListSerializer, MessageCreateSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django.db.models import Q

class MessageCreate(generics.CreateAPIView):
    queryset = Collaborate_Messaging_A00.objects.all()
    lookup_field = 'Collaborate_Messaging_A00_Rec'
    serializer_class = MessageCreateSerializer

    def get_queryset(self):
        #check=Collaborate_Files_A00.objects.values_list('collaborate_files_a00_rec', 'file_name')
        #print(check) #to be imported in a repository
        return Collaborate_Messaging_A00.objects.all()

class MessageReadUpdate(generics.RetrieveUpdateAPIView):
    lookup_field = 'Collaborate_Messaging_A00_Rec'
    serializer_class = FUMSerializer

    def get_queryset(self):
        return Collaborate_Messaging_A00.objects.all()



class MessageListAPIView(generics.ListAPIView):
    serializer_class = MessageListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['message', 'messageType', 'dateTimeStamp',]

    def get_queryset(self, *args, **kwargs):
        queryset_list = Collaborate_Messaging_A00.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(message__icontains=query)|
                Q(messageType__icontains=query)|
                Q(dateTimeStamp__icontains=query)

            ).distinct()
        return queryset_list