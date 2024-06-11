from django.urls import *
from almacenes import views
from almacenes.views import *

urlpatterns = [
    path('', Home1.as_view(), name='login1'),
]