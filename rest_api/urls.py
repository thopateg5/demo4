from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView 
from .views import DeleteView
from .views import nnd 
from .views import nnd_list
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'bucketlist',DeleteView)
urlpatterns = {
    url(r'^bucketlists/$', CreateView.as_view(), name="create"),
    #url(r'^list/', ListAPIView.as_view(), name="create1"),
    url(r'^bucketlist/delete/(?P<pk>[0-9]+)/$', DeleteView.as_view(), name="delete"),
   # url(r'^bucketlists/delete/(?P<pk>[0-9]+)/$',DeleteView.as_view(), name="Delete"),
    url(r'^bucketlists/nnd/',nnd.as_view(), name="Delete"),  
    url(r'^bucketlists/nnd_list/',nnd_list.as_view(), name="list"), 
   # url('bucketlists/', include('rest_framework.urls', namespace='rest_framework'))


}
    
urlpatterns = format_suffix_patterns(urlpatterns)