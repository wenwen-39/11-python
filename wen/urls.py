
from django.contrib import admin
from django.urls import path
from mainsite.views import homepage, homepage1,maps_mod

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('place/<int:place>/', homepage1),
    path('maps/<str:la>,<str:lo>/', maps_mod),

]
