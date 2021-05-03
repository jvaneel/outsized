from rest_framework import routers
from outsized.core.views import *

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

router = routers.DefaultRouter()
router.register('clients', ClientViewSet , basename='clients')
router.register('stakeholders', StakeholderViewSet , basename='stakeholders')