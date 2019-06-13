from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from get_secrets import *

def main():
    resp = MessagingResponse()

    resp.message ("You have reached the DogBot. Thanks for contacting us :)")

    return str(resp)

if __name__ == "__main__":
    main()
