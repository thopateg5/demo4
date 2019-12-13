
#from rest_framework import routers
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import Selected_Device 
from .views import All_Device

urlpatterns = {
    url(r'^Selected_Device/',Selected_Device.as_view(), name="Delete"),  
    url(r'^All_Device/',All_Device.as_view(), name="list")     
}
    
urlpatterns = format_suffix_patterns(urlpatterns)

















# urlpatterns = {
#    # url(r'^bucketlists/$', CreateView.as_view(), name="create"),
#     #url(r'^list/', ListAPIView.as_view(), name="create1"),
#     #url(r'^bucketlist/delete/(?P<pk>[0-9]+)/$', DeleteView.as_view(), name="delete"),
#    # url(r'^bucketlists/delete/(?P<pk>[0-9]+)/$',DeleteView.as_view(), name="Delete"),
#     url(r'^bucketlists/Selected_Device/',Selected_Device.as_view(), name="Delete"),  
#     url(r'^bucketlists/All_Device/',All_Device.as_view(), name="list"), 
#     #url(r'^bucketlists/Delete_All_Device/',Delete_All_Device.as_view(), name="list"), 
#    # url('bucketlists/', include('rest_framework.urls', namespace='rest_framework'))


# }