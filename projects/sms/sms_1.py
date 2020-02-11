from twilio.rest import Client

with open('auth_keys.txt', 'r') as file:
    account_sid = file.readline().strip()
    auth_token = file.readline().strip()

print(account_sid, auth_token)
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hello my self',
                              from_='****',
                              to='****')
