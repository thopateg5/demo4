from rest_framework import generics
from .serializers import BucketlistSerializer
from .models import Bucketlist
from .devicemanager import DeviceManager
import requests
from django.http import QueryDict
import json
from django.http import HttpResponse

connectionString = 'HostName=newmyiothub.azure-devices.net;SharedAccessKeyName=iothubowner;SharedAccessKey=7m1wTjgz4bgjPtTpRoV/fLhH3m73o9j9J0qtaJ9DJSU='
dm = DeviceManager(connectionString)	

class CreateView(generics.ListCreateAPIView):
    queryset = Bucketlist.objects.all()
   # for my_bucket_object in Bucketlist.objects.all():
    #    print(type(my_bucket_object))    
    serializer_class = BucketlistSerializer
    def perform_create(self, serializer):                   
        deviceId = 'rohit01'          
        dm.createDeviceId(deviceId)    
        serializer.save()


class DeleteView(generics.RetrieveDestroyAPIView):
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    
    def perform_destroy(self, serializer): 
        print ("IN deleteview function")
        dm.listDeviceIds()        
        print("..............")
        #print (description)
        print("..............")
        print (self)
        print("..............")

    def delete(self,request):
        print ("delete Ok")
        
class nnd(generics.RetrieveDestroyAPIView):

    def delete(self,request):
        person_dict = json.loads(request.body)
        #print(person_dict['name'])
        deviceId = person_dict['name']           
        responce_from_azure = dm.deleteDeviceId(deviceId)
        return  HttpResponse(responce_from_azure)
        
        
    def post(self, request):
        print(request.body)
        person_dict = json.loads(request.body)       
        deviceId = person_dict['name']          
        responce_from_azure = dm.createDeviceId(deviceId)        
        return  HttpResponse(responce_from_azure)
       

            
    def get(self, request):
        print(request.body)
        person_dict = json.loads(request.body)       
        deviceId = person_dict['name']          
        responce_from_azure = dm.retrieveDeviceId(deviceId)        
        return HttpResponse(responce_from_azure)

       
class nnd_list(generics.ListAPIView):
    print(".........................\n\n")
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    def perform_create(self, request):     
        responce_from_azure = dm.listDeviceIds() 
        print(".........................\n\n")
        print(responce_from_azure)      
        request.save()
        return HttpResponse(responce_from_azure)


    


# class create1(generics.ListCreateAPIView):
#     """This class defines the create behavior of our rest api."""
#     queryset = Bucketlist.objects.all()
#     serializer_class = BucketlistSerializer

#     def perform_create(self, serializer):
#         print("HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
#         """Save the post data when creating a new bucketlist."""
#         # IoT DeviceID
#         deviceID = "myDevice09"
#         # Iot Hub Name
#         IoTHubName = "newmyiothub"
#         # RestAPI Version
#         iotHubAPIVer = "2018-06-30"
#         iotHubRestURI = "https://" + IoTHubName + ".azure-devices.net/devices/" + deviceID + "?api-version=" + iotHubAPIVer
#         # SAS Token Generated via Azure CLI or Device Explorer
#         SASToken = 'SharedAccessSignature sr=newmyiothub.azure-devices.net&sig=657IPbiCv0PUe1weYeCSGJKW%2BsTrZni0Jqu8EiANpbY%3D&skn=iothubowner&se=1576069307'

#         # Headers
#         Headers = {}
#         Headers['Authorization'] = SASToken
#         Headers['Content-Type'] = "application/json"

#         # Message Payload        
#         body = {} 
#         body['deviceid'] = deviceID 

#         # Send Message
#         resp = requests.put(iotHubRestURI, json=body, headers=Headers)
#         print(iotHubRestURI)
#         print(resp)
#         #serializer.save()


# class delete1(generics.ListCreateAPIView):
#     """This class defines the create behavior of our rest api."""
#     queryset = Bucketlist.objects.all()
#     serializer_class = BucketlistSerializer

#     def perform_destroy(self, serializer):
#         # IoT DeviceID
#         deviceID = "myDevice09"
#         # Iot Hub Name
#         IoTHubName = "newmyiothub"
#         # RestAPI Version
#         iotHubAPIVer = "2018-06-30"
#         iotHubRestURI = "https://" + IoTHubName + ".azure-devices.net/devices/" + deviceID + "?api-version=" + iotHubAPIVer
#         # SAS Token Generated via Azure CLI or Device Explorer
#         SASToken = 'SharedAccessSignature sr=newmyiothub.azure-devices.net&sig=657IPbiCv0PUe1weYeCSGJKW%2BsTrZni0Jqu8EiANpbY%3D&skn=iothubowner&se=1576069307'

#         # Headers
#         Headers = {}
#         Headers['Authorization'] = SASToken
#         Headers['Content-Type'] = "application/json"
#         Headers['If-Match']= '*'

#         # Message Payload
#         #Sdatetime =  datetime.datetime.now()
#         body = {} 
#         body['deviceid'] = deviceID 

#         # Send Message
#         resp = requests.delete(iotHubRestURI, headers=Headers)
#         print(iotHubRestURI)
#         print(resp)



# # final testing....................datetime A combination of a date and a time. Attributes: ()
