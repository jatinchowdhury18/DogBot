import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
from get_images import get_image_urls
from get_secrets import *
import random

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
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client (get_account_sid(), get_auth_token(), http_client=proxy_client)

    query = get_query()
    url = random.choice (get_image_urls (query))

    twilio_number = get_Twilio_number()
    phone_numbers = get_phone_numbers()

    for number in phone_numbers:
        message = client.messages.create (from_=twilio_number, media_url=url, to=number)
        print (message.sid)

if __name__ == "__main__":
    main()
