import base64
from datetime import datetime
import requests
import keys
from requests.auth import HTTPBasicAuth


unformatted_time = datetime.now()
formatted_time = unformatted_time.strftime("%Y%m%d%H%M%S")

data_to_encode = keys.business_short_code + keys.LNM_passkey + formatted_time
encoded = base64.b64encode(data_to_encode.encode())
decoded_password = encoded.decode('utf-8')

consumer_key = keys.consumer_key
consumer_secret = keys.consumer_secret
api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
r = requests.get(api_URL,auth=HTTPBasicAuth(consumer_key,consumer_secret))

# print (r.json())
json_response = r.json()
my_ccess_token = json_response['access_token']

# print(access_token)

def lipa_na_mpesa():
    access_token = my_ccess_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer %s' % access_token
    # 'Authorization': 'Bearer LCXsWuHBoKjjsacHricBk39SxDh5'

    }
    request = {
        "BusinessShortCode": keys.business_short_code,
        "Password": decoded_password,
        "Timestamp": formatted_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": 1,
        "PartyA": keys.partyA,
        "PartyB": keys.business_short_code,
        "PhoneNumber": keys.phone_number,
        "CallBackURL": "https://mydomain.com/path",
        "AccountReference": "TechIT Ltd",
        "TransactionDesc": "Payment fees" 
    }
    response = requests.post(api_url,json=request,headers=headers)
    # response = requests.request("POST", 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest', headers = headers, data = payload)
    print(response.text)

    # print(response.text.encode('utf8'))

lipa_na_mpesa()