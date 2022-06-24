from .views import UserViewSet, ClientViewSet, ConversationViewSet, MessageViewSet, UploadDataViaCSV
from django.conf.urls import include
from rest_framework import routers
from django.urls import path

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('clients', ClientViewSet)
router.register('conversations', ConversationViewSet)
router.register('messages', MessageViewSet)
router.register('csv', UploadDataViaCSV, basename="upload_clients")

urlpatterns = [
    path('', include(router.urls)),
]
