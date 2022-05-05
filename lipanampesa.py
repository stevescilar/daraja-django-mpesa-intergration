import base64
from datetime import datetime
import requests
import keys



unformatted_time = datetime.now()
formatted_time = unformatted_time.strftime("%Y%m%d%H%M%S")

data_to_encode = keys.busines_short_code + keys.LNM_passkey + formatted_time
encoded = base64.b64encode(data_to_encode.encode())
decoded_password = encoded.decode('utf-8')

def lipa_na_mpesa():
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer LCXsWuHBoKjjsacHricBk39SxDh5'
    }
    payload = {
        "BusinessShortCode": keys.busines_short_code,
        "Password": decoded_password,
        "Timestamp": formatted_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": 1,
        "PartyA": keys.phone_number,
        "PartyB": keys.busines_short_code,
        "PhoneNumber": keys.phone_number,
        "CallBackURL": "https://mydomain.com/path",
        "AccountReference": "CompanyXLTD",
        "TransactionDesc": "Payment of 1" 
    }
    response = requests.request("POST", 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest', headers = headers, data = payload)

    print(response.text.encode('utf8'))