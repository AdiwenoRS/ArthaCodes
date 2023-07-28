import json
import requests

response = requests.get('https://api.open-notify.org/iss-pass.json')

print (response.status_code)

def jprint(obj):
    test = json.dumps(obj, sort_keys=True, indent=4)
    print(test)

jprint(response.json())

{
    "message": "success",
    "number": 6,
    "people": [
        {
            "craft": "ISS",
            "name": "Alexey Ovchinin"
        },
        {
            "craft": "ISS",
            "name": "Nick Hague"
        },
        {
            "craft": "ISS",
            "name": "Christina Koch"
        },
        {
            "craft": "ISS",
            "name": "Alexander Skvortsov"
        },
        {
            "craft": "ISS",
            "name": "Luca Parmitano"
        },
        {
            "craft": "ISS",
            "name": "Andrew Morgan"
        }
    ]
}
