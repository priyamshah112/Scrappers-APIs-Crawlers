from twilio.rest import Client 
 
account_sid = 'Account sid' 
auth_token = 'Auth Key'
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='Twilio Number',        
                              to='Receiver Number' ,
                              body='Hi Priyam Twilio'
                          ) 
 
print(message.sid)
