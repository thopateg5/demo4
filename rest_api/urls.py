from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, create1,delete1

urlpatterns = {
    url(r'^bucketlists/$', CreateView.as_view(), name="create"),
    url(r'^create$', create1.as_view(), name="create"),
    url(r'^delete$', delete1.as_view(), name="create"),
}

urlpatterns = format_suffix_patterns(urlpatterns)