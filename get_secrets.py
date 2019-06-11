def get_secret (key):
    file = open ("secrets.txt", 'r')
    secrets = file.read().splitlines()
    file.close()

    for i in range (len (secrets)):
        if secrets[i] == "# " + key:
            return secrets[i+1]
    
    print ("Invalid key!!")

def get_account_sid():
    return get_secret ('account_sid')

def get_auth_token():
    return get_secret ("auth_token")

def get_Twilio_number():
    return get_secret ("twilio_number")
