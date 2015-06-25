# -*- coding: utf-8 -*-
import requests, json

# create the header
appId = 'NtKF1qDEmxpwm2OWLc2rFbxfDfetUAnfu4NRfZVF' 
apiKey = 'xoSxmJk7Ejaux6juwZxSDyBQcT8WjmJhag4fTzL8' 
headers = {'Content-Type': 'application/json', 'X-Parse-Application-Id': appId, 'X-Parse-REST-API-Key': apiKey}

# edit to create the object
spanish = "lavadora"
english = "washing machine"
speech = "feminine noun"
ex_span = "La secadora todavía funciona, pero necesitamos comprar una lavadora nueva."
ex_eng = "The dryer still works, but we have to buy a new washing machine." 

# post
url = "https://api.parse.com/1/classes/Card"
data = {'spanish': spanish, 'english': english, 'speech': speech, 'ex_span': ex_span, 'ex_eng': ex_eng}
r = requests.post(url, headers=headers, data=json.dumps(data))
print r.json()
