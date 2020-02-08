import requests

import hashlib
import sys

# using SHA1 Hash
# Hash is only one way function
# using anonymous key, sending only the 5 characters
# The API will return the matches and how many times was pwned
# The program will check if matches with the entere pwd and shows the result.


def request_api_data(querychar):
    """
    the api checks if there is hashs with the same 5 first characters(in sha1)
    and send back all matches. But will return without the 5 frist characters.
    """
    if not(isinstance(querychar, str)):
        print('The password must be string!')
        return
    url = f'https://api.pwnedpasswords.com/range/{querychar}'
    r = requests.get(url)
    if r.status_code != 200:
        raise RuntimeError(f"Error fetching: {r.status_code}, check the api and try again")
    return r


def get_pass_leaks_count(hashes, hash_to_check):
    hashs = (line.split(':') for line in hashes.text.splitlines())
    # will return a generator with tuples and each tuple has the hash and number
    for h, count in hashs:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    # check password if it exists in API response
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    #password.encode transform into b''
    first5, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5)
    # return read_res(response)
    return get_pass_leaks_count(response, tail)


def main(args):
    for pwd in args:
        count = pwned_api_check(pwd)
        if count:
            print(f"{pwd} was found {count} times... you should change your password")
        else:
            print(f"{pwd} was not found! Nice!")
    return 'Done!'

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
    