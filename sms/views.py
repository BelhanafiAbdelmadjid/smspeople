from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from twilio.twiml.messaging_response import MessagingResponse


class ReceiveSMSAPIView(APIView):
    def get(self,request):
        """Respond to incoming calls with a simple text message."""
        # Start our TwiML response
        resp = MessagingResponse()

        # Add a message
        resp.message("The Robots are coming! Head for the hills!")

        return Response('Hello world',status=status.HTTP_200_OK)
# Create your views here.
