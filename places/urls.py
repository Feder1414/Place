from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt

from .views import PlaceList,PlaceCreate

urlpatterns = [ path('places/', PlaceList, name='places'),
                path('placecreate/', csrf_exempt(PlaceCreate), name='placecreate')
              ]