from twilio.rest import TwilioRestClient 
 
# put your own credentials here 
ACCOUNT_SID = "AC704c52f848ac4a38e1c79c261fb5be1a" 
AUTH_TOKEN = "df21f1a9fdc7e380b9e121c702dfb954" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 
#client.messages.create(
#	to="206-478-4652", 
	#from_="+12068666887", 
	#body=raw_input("SMS Body: "),  
#)

def sendSMS(receiver, body):
    client.messages.create(
	    to=receiver, 
	    from_="+12068666887", 
	    body=body,  
    )
