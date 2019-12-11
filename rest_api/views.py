from rest_framework import generics
from .serializers import BucketlistSerializer
from .models import Bucketlist
import requests 


class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

class create1(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer

    def perform_create(self, serializer):
        print("HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        """Save the post data when creating a new bucketlist."""
        # IoT DeviceID
        deviceID = "myDevice09"
        # Iot Hub Name
        IoTHubName = "newmyiothub"
        # RestAPI Version
        iotHubAPIVer = "2018-06-30"
        iotHubRestURI = "https://" + IoTHubName + ".azure-devices.net/devices/" + deviceID + "?api-version=" + iotHubAPIVer
        # SAS Token Generated via Azure CLI or Device Explorer
        SASToken = 'SharedAccessSignature sr=newmyiothub.azure-devices.net&sig=657IPbiCv0PUe1weYeCSGJKW%2BsTrZni0Jqu8EiANpbY%3D&skn=iothubowner&se=1576069307'

        # Headers
        Headers = {}
        Headers['Authorization'] = SASToken
        Headers['Content-Type'] = "application/json"

        # Message Payload        
        body = {} 
        body['deviceid'] = deviceID 

        # Send Message
        resp = requests.put(iotHubRestURI, json=body, headers=Headers)
        print(iotHubRestURI)
        print(resp)
        #serializer.save()


class delete1(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer

    def perform_create(self, serializer):
        # IoT DeviceID
        deviceID = "myDevice09"
        # Iot Hub Name
        IoTHubName = "newmyiothub"
        # RestAPI Version
        iotHubAPIVer = "2018-06-30"
        iotHubRestURI = "https://" + IoTHubName + ".azure-devices.net/devices/" + deviceID + "?api-version=" + iotHubAPIVer
        # SAS Token Generated via Azure CLI or Device Explorer
        SASToken = 'SharedAccessSignature sr=newmyiothub.azure-devices.net&sig=657IPbiCv0PUe1weYeCSGJKW%2BsTrZni0Jqu8EiANpbY%3D&skn=iothubowner&se=1576069307'

        # Headers
        Headers = {}
        Headers['Authorization'] = SASToken
        Headers['Content-Type'] = "application/json"
        Headers['If-Match']= '*'

        # Message Payload
        #Sdatetime =  datetime.datetime.now()
        body = {} 
        body['deviceid'] = deviceID 

        # Send Message
        resp = requests.delete(iotHubRestURI, headers=Headers)
        print(iotHubRestURI)
        print(resp)