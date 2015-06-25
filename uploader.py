# -*- coding: utf-8 -*-
import requests, json, httplib

appId = 'NtKF1qDEmxpwm2OWLc2rFbxfDfetUAnfu4NRfZVF' 
apiKey = 'xoSxmJk7Ejaux6juwZxSDyBQcT8WjmJhag4fTzL8' 

# change these
cid = 1
spanish = "lavadoro"
english = "washing machine"
speech = "feminine noun"
ex_span = "La secadora todavía funciona, pero necesitamos comprar una lavadora nueva."
ex_eng = "The dryer still works, but we have to buy a new washing machine." 
imageName = "noun_118.png"

# upload the image
connection = httplib.HTTPSConnection('api.parse.com', 443)
connection.connect()
connection.request('POST', '/1/files/' + imageName, open(imageName, 'rb').read(), {
       "X-Parse-Application-Id": appId,
       "X-Parse-REST-API-Key": apiKey,
       "Content-Type": "image/png"
     })
result = json.loads(connection.getresponse().read())

connection = httplib.HTTPSConnection('api.parse.com', 443)
connection.connect()
connection.request('POST', '/1/classes/Card', json.dumps({
       "cid": cid,
       "spanish": spanish,
       "english": english, 
       "speech": speech, 
       "ex_span": ex_span,
       "ex_eng": ex_eng,
       "picture": {
         "name": result['name'],
         "__type": "File"
       }
     }), {
       "X-Parse-Application-Id": appId,
       "X-Parse-REST-API-Key": apiKey,
       "Content-Type": "application/json"
     })
result = json.loads(connection.getresponse().read())
print result
