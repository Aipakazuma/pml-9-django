from django.conf.urls import url
from form import views
from form.views import IndexView


urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index')
]

