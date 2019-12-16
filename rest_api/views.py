#from .serializers import BucketlistSerializer
#from .models import Bucketlist
#import requests
#from django.http import QueryDict
from rest_framework import generics
from .devicemanager import DeviceManager
import json
from django.http import HttpResponse
from .datamasemanagement import DatabaseManagement


#connectionString = 'HostName=newmyiothub.azure-devices.net;SharedAccessKeyName=iothubowner;SharedAccessKey=7m1wTjgz4bgjPtTpRoV/fLhH3m73o9j9J0qtaJ9DJSU='
#connectionString = 'HostName=demo4IoTHub.azure-devices.net;SharedAccessKeyName=iothubowner;SharedAccessKey=/jbP/V4KmH/hvg7FvmTcaVMKp2sBZVsGPn1dwR8pPMo='
connectionString = 'HostName=demo4IoTHub.azure-devices.net;SharedAccessKeyName=iothubowner;SharedAccessKey=/jbP/V4KmH/hvg7FvmTcaVMKp2sBZVsGPn1dwR8pPMo='
dm = DeviceManager(connectionString)
dm1 = DatabaseManagement()

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
 
       
class All_Device(generics.RetrieveDestroyAPIView):
    
    def get(self, request): 
        responce_from_azure = dm.listDeviceIds()     #dm.retrieveDeviceId(deviceId)  
        return HttpResponse(responce_from_azure)
           

    def delete(self, request):
        responce_from_azure = dm.DeletelistDevice()         
        return HttpResponse(responce_from_azure)


class less_than_temp(generics.ListAPIView):
    
    def get(self, request): 
        person_dict = json.loads(request.body)       
        deviceId = person_dict['value']  
        responce_from_azure = dm1.temp_less_than(deviceId) 
        #responce_from_azure = dm.listDeviceIds()     #dm.retrieveDeviceId(deviceId)  
        return HttpResponse(responce_from_azure)

class greater_than_temp(generics.ListAPIView):
    
    def get(self, request): 
        person_dict = json.loads(request.body)       
        vlaue = person_dict['value']  
        responce_from_azure = dm1.temp_greater_than(vlaue) 
        #responce_from_azure = dm.listDeviceIds()     #dm.retrieveDeviceId(deviceId)  
        return HttpResponse(responce_from_azure)

class between_humidity(generics.ListAPIView):

    def get(self, request): 
        person_dict = json.loads(request.body)       
        min_val = person_dict['low'] 
        max_val = person_dict['high'] 
        responce_from_azure = dm1.humidity_in_between(min_val, max_val) 
        #responce_from_azure = dm.listDeviceIds()     #dm.retrieveDeviceId(deviceId)  
        return HttpResponse(responce_from_azure)

class between_time(generics.ListAPIView):
    
    def get(self, request): 
        person_dict = json.loads(request.body)       
        min_val = person_dict['low'] 
        max_val = person_dict['high'] 
        responce_from_azure = dm1.between_time(min_val, max_val) 
        #responce_from_azure = dm.listDeviceIds()     #dm.retrieveDeviceId(deviceId)  
        return HttpResponse(responce_from_azure)



#.................this is for custome container access........................................

# class less_than_temp1(generics.ListAPIView):
    
#     def get(self, request): 
#         person_dict = json.loads(request.body)       
#         g = person_dict['value'] 
#         data = person_dict['container']   #'DeviceData'
#         query1 = 'SELECT '+data+'.temperature, '+data+'.humidity, '+data+'.preasure   FROM  '+data+'  WHERE '+data+'.temperature<'+g
#         responce_from_azure = dm1.get_item1(query1,data) 
#         #responce_from_azure = dm.listDeviceIds()     #dm.retrieveDeviceId(deviceId)  
#         return HttpResponse(responce_from_azure)

# class greater_than_temp1(generics.ListAPIView):
        
#     def get(self, request): 
#         person_dict = json.loads(request.body)       
#         g = person_dict['value'] 
#         data = person_dict['container']   #'DeviceData'
#         query1 = 'SELECT '+data+'.temperature, '+data+'.humidity, '+data+'.preasure   FROM  '+data+'  WHERE '+data+'.temperature>'+g
#         responce_from_azure = dm1.get_item1(query1,data) 
#         #responce_from_azure = dm.listDeviceIds()     #dm.retrieveDeviceId(deviceId)  
#         return HttpResponse(responce_from_azure)

# class between_humidity1(generics.ListAPIView):
    
#     def get(self, request): 
#         person_dict = json.loads(request.body)       
#         min_val = person_dict['min_val'] 
#         max_val = person_dict['max_val']
#         data = person_dict['container']   #'DeviceData'
#         query1 = 'SELECT '+data+'.temperature, '+data+'.humidity, '+data+'.preasure   FROM  '+data+'  WHERE '+data+'.humidity BETWEEN '+min_val+'  AND '+max_val  
#         responce_from_azure = dm1.get_item1(query1,data) 
#         #responce_from_azure = dm.listDeviceIds()     #dm.retrieveDeviceId(deviceId)  
#         return HttpResponse(responce_from_azure)

    
# class between_time1(generics.ListAPIView):
        
#     def get(self, request): 
#         person_dict = json.loads(request.body)       
#         min_val = person_dict['min_val'] 
#         max_val = person_dict['max_val']
#         data = person_dict['container']   #'DeviceData'
#         query1 = 'SELECT '+data+'.temperature, '+data+'.humidity, '+data+'.preasure   FROM  '+data+'  WHERE '+data+'.gateway_ts BETWEEN '+min_val+'  AND '+max_val  
#         responce_from_azure = dm1.get_item1(query1,data) 
#         #responce_from_azure = dm.listDeviceIds()     #dm.retrieveDeviceId(deviceId)  
#         return HttpResponse(responce_from_azure)






