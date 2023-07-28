import requests

response = requests.get('https://google.com/')

print (response.status_code)

if response:
    print("Response")
