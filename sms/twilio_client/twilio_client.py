from twilio.rest import Client
import json
from datetime import datetime

class TwilioDJ():
    # MY_PHONE_NUMBER = "+16466667185"
    # ACCOUNT_SID = "AC0c72df4b7c94c8ab471c5092643b2929"
    # AUTH_TOKEN = "a9aeab16f1264c9755765cd09434bad1"

    MY_PHONE_NUMBER = "+19099069942"
    ACCOUNT_SID = "ACe3e02549389e9b453f08b5136f64d4eb"
    AUTH_TOKEN = "e74b311d655c8d5a815c5f9be4a1d18b"

    CLIENT = Client(ACCOUNT_SID, AUTH_TOKEN)
    def make_conv(self,target):

        '''
        This would query all message from "target" number and then make a list that represents a conversation
        conversation = [
            {
                "from_target" : True,
                "date" : 21/03/2005/21h,
                "content" : "The message here"
            },
            {
                "from_target" : False,
                "date" : 21/03/2005/22h,
                "content" : "The message here"
            }
        ]
        '''
        list = self.CLIENT.messages.list(
                to="+213554575471",
            )
        conversation = sorted(
            [
                {
                    "from_target": message.from_ != self.MY_PHONE_NUMBER,
                    "date": message.date_sent.strftime("%d/%m/%Y/%Hh/%Mm/%Ss"),
                    "content": message.body
                }
                for message in list
            ],
            key=lambda x: datetime.strptime(x["date"], "%d/%m/%Y/%Hh/%Mm/%Ss")
        )
        return conversation
       

           
    def make_context(self,messages):
        '''
        This would take the context and gather the next peace of information
        '''

    def send_message(self,target,message):
        # "+213554575471"
        # "This is the ship that made the Kessel Run in fourteen parsecs?"
        '''
        This would answer the phone number with a text message
        '''
        self.CLIENT.messages.create(
            body=message,
            from_=self.MY_PHONE_NUMBER,
            to=target,
        )
        pass


if __name__ == "__main__" :
    
    pass



    