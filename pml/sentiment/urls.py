from django.conf.urls import url
from sentiment import views
from sentiment.views import IndexView


urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^registry/$', views.registry, name='registry'),
]

