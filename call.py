from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACc66fe0075075f72b524ab702fcd4c492"
auth_token  = "b1ad8841e8c162b46f5c598611fded97"
client = TwilioRestClient(account_sid, auth_token)

call = client.calls.create(url="http://demo.twilio.com/docs/voice.xml",
    to="+260965175641",
    from_="+15017250604")
print(call.sid)