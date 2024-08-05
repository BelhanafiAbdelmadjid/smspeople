from sms.views import ReceiveSMSAPIView,SendSMSAPIVew
from django.urls import path

urlpatterns = [
    path('sms/receive', ReceiveSMSAPIView.as_view(),name="sms_receive_webhook"),
    path('sms/send', SendSMSAPIVew.as_view(),name="sms_send_webhook"),
]
