#from .serializers import BucketlistSerializer
#from .models import Bucketlist
#import requests
#from django.http import QueryDict
from rest_framework import generics
from .devicemanager import DeviceManager
import json
from django.http import HttpResponse

connectionString = 'HostName=newmyiothub.azure-devices.net;SharedAccessKeyName=iothubowner;SharedAccessKey=7m1wTjgz4bgjPtTpRoV/fLhH3m73o9j9J0qtaJ9DJSU='
dm = DeviceManager(connectionString)	

class Selected_Device(generics.RetrieveDestroyAPIView):

    def delete(self,request):
        person_dict = json.loads(request.body)
        deviceId = person_dict['name']           
        responce_from_azure = dm.deleteDeviceId(deviceId)
        return  HttpResponse(responce_from_azure)
        
        
    def post(self, request):
        person_dict = json.loads(request.body)       
        deviceId = person_dict['name']          
        responce_from_azure = dm.createDeviceId(deviceId)        
        return  HttpResponse(responce_from_azure)   

            
    def get(self, request):
        person_dict = json.loads(request.body)       
        deviceId = person_dict['name']          
        responce_from_azure = dm.retrieveDeviceId(deviceId)    # dm.listDeviceIds()    
        return HttpResponse(responce_from_azure)
 
       
class All_Device(generics.ListAPIView):
    
    def get(self, request): 
        responce_from_azure = dm.listDeviceIds()     #dm.retrieveDeviceId(deviceId)  
        return HttpResponse(responce_from_azure)

    def delete(self, request):
        responce_from_azure = dm.DeletelistDevice() 
        return HttpResponse(responce_from_azure)









# class Delete_All_Device(generics.RetrieveDestroyAPIView):
    
#     def delete(self, request):     
#         #print(request.body)
#         person_dict = json.loads(request.body)       
#         deviceId = person_dict['name']          
#         responce_from_azure = dm.DeletelistDevice() 
#         return HttpResponse(responce_from_azure)


# class CreateView(generics.ListCreateAPIView):
#     queryset = Bucketlist.objects.all()   
#     serializer_class = BucketlistSerializer
#     def perform_create(self, serializer):                   
#         deviceId = 'rohit01'          
#         dm.createDeviceId(deviceId)    
#         serializer.save()
# class DeleteView(generics.RetrieveDestroyAPIView):
#     queryset = Bucketlist.objects.all()
#     serializer_class = BucketlistSerializer    
#     def perform_destroy(self, serializer): 
#         dm.listDeviceIds()        
#     def delete(self,request):
#         print ("delete Ok")