import imaplib, email

user = '****'
pwd = '****'
imap_url = 'imap.gmail.com'

conn = imaplib.IMAP4_SSL(imap_url)

conn.login(user,pwd)

print(conn.list()) # list all folders

print(conn.select("INBOX")) #select the folder

result, data = conn.uid("search", None, "ALL") # search emails data

print(result, data) # return the emails ids in bytes string

ids = data[0].split()
last_one = ids[-1]
oldest_one = ids[0]
print(last_one)
result2, email_data = conn.uid("fetch", last_one, '(RFC822)')
print(email_data)

raw_email = email_data[0][1].decode('utf-8')
email_message = email.message_from_string(raw_email)

print(dir(email_message))
print(email_message['Subject'])




