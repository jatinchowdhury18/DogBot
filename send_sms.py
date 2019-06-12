import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
from get_images import get_image_urls
from get_secrets import *
import random
from datetime import datetime

def get_query():
    file = open ("queries.txt", 'r')
    queries = file.read().splitlines()
    file.close()
    return random.choice (queries)

def get_phone_numbers():
    file = open ("phone_numbers.txt", 'r')
    phone_numbers = file.read().splitlines()
    file.close()
    return phone_numbers

def main():
    # get time (Pacific)
    time = (datetime.utcnow().time().hour - 7) % 24
    print ("[Trigger]: Hour {}".format (time))

    # only run if not in the middle of the night
    if time in [0, 1, 2, 3, 4, 5, 6, 7]:
        print ("[Skipping]: Late at night")
        return

    # set up Twilio client
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client (get_account_sid(), get_auth_token(), http_client=proxy_client)

    # set up phone numbers
    twilio_number = get_Twilio_number()
    phone_numbers = get_phone_numbers()

    num_sent = 0
    for number in phone_numbers:
        # Google search
        query = get_query()
        url = random.choice (get_image_urls (query))
        print ("[Query]: {}".format (query))

        # send message
        try:
            message = client.messages.create (from_=twilio_number, media_url=url, to=number)
            num_sent += 1
            print ("[Sending]: {}".format (message.sid))
        except:
            pass

    print ("[Messages succesful]: {}".format (num_sent))

if __name__ == "__main__":
    main()
