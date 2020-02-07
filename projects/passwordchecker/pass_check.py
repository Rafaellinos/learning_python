import requests

import hashlib
# using SHA1 Hash
# Hash is only one way function
# using anonymous key, sending only the 5 characters
"""
the api checks if there is hashs with the same 5 first characters
and send back all of those to check with our full hash.
"""

def request_api_data(querychar):
    if not(isinstance(querychar, str)):
        print('The password must be string!')
        return
    url = f'https://api.pwnedpasswords.com/range/{querychar}'
    r = requests.get(url)
    if r.status != 200:
        raise RuntimeError(f"Error fetching: {r.status_code}, check the api and try again")

def pwned_api_check(password):
    # check password if it exists in API response
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    #password.encode transform into b''
    print(sha1password)
    return sha1password

pwned_api_check('123213')
    