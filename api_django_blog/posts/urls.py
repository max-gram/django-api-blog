from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, DetailsView

urlpatterns = {
	url(r'^posts/(?P<pk>[0-9]+)/$', DetailsView.as_view(), name="details"),
    url(r'^posts/$', CreateView.as_view(), name="create"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
