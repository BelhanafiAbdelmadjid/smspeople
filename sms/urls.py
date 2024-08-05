from sms.views import ReceiveSMSAPIView
from django.urls import path

urlpatterns = [
    path('sms/receive', ReceiveSMSAPIView.as_view(),name="sms_receive_webhook"),
]
