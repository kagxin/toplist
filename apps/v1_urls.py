from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('demo/', include('apps.demo.urls')),
    path('schedule/', include('apps.schedule.urls'))
]