import requests

headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer QOA5tKVb0TRXMO35iyOmsVkKQqWs'
}

payload = {
    "BusinessShortCode": 174379,
    "Password": "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMjIwNTA1MTcyMzAz",
    "Timestamp": "20220505172303",
    "TransactionType": "CustomerPayBillOnline",
    "Amount": 1,
    "PartyA": 254708374149,
    "PartyB": 174379,
    "PhoneNumber": 254705549257,
    "CallBackURL": "https://mydomain.com/path",
    "AccountReference": "CompanyXLTD",
    "TransactionDesc": "Payment of X" 
  }

response = requests.request("POST", 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest', headers = headers, data = payload)
print(response.text)