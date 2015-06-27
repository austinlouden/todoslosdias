# -*- coding: utf-8 -*-
import requests, json, httplib

appId = 'NtKF1qDEmxpwm2OWLc2rFbxfDfetUAnfu4NRfZVF' 
apiKey = 'xoSxmJk7Ejaux6juwZxSDyBQcT8WjmJhag4fTzL8' 

# feminine
# masculine
# change these
cid = 15
spanish = "cepillo de dientes"
english = "toothbrush"
speech = "masculine noun"
ex_span = "siempre se me olvida empacar el cepillo de dientes"
ex_eng = "I always forget to pack my toothbrush" 
imageName = "noun_1827.png"

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
