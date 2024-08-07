from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from twilio.twiml.messaging_response import MessagingResponse
from .twilio_client.twilio_client import TwilioDJ



class ReceiveSMSAPIView(APIView):
    def post(self,request):
        f = open("./logs","w")
        f.writelines("\n".join([f'{str(item)} : {str(request.data[item])}' for item in list(request.data.keys())]))

        # Start our TwiML response
        resp = MessagingResponse()

        # Determine the right reply for this message
        # if body == 'hello':
        #     resp.message("Hi!")
        # elif body == 'bye':
        #     resp.message("Goodbye")
        return Response(str(resp),status=status.HTTP_200_OK)

class SendSMSAPIVew(APIView):
    def post(self,request):
        tdj = TwilioDJ()
        # "+213554575471"
        # "This is the ship that made the Kessel Run in fourteen parsecs?"
        tdj.send_message(
            target="+19099069942",
            message="This is the ship that made the Kessel Run in fourteen parsecs?"
        )
        return Response("Sent success",status=status.HTTP_201_CREATED)

