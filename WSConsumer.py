#!/usr/bin/python
# -*- coding: utf-8 -*-
from json import dumps
import requests

# Send data to web service, passing a JSON object as INPUT
def sendJson(payload, url = 'http://192.168.45.156/sensores/web/medidas', type = 'json'):

  if type == 'json':
    headers = {'content-type': 'application/json'}
  elif type == 'xml':
    headers = {'content-type': 'application/xml'}
  else:
    print "unknown content type"
    return -1

  r = requests.post(url, data=dumps(payload), headers=headers)

  print(r.json())
  return 1

# Send data to web service, passing each value (one by one)
# date = String with any valid date format.
# band = small integer (probably not the right format, we did not know about this).
# value = Any number.
# sensor_id = valid ids, as of 05.04.15 numbers from 1 to 4, to add other sensors go to: http://192.168.45.156/sensores/web/sensor.
# type_id = 1, 2 or 3, as of 05.04.15 this is a dummy column (it probably makes no sense).
# comment = Optional, any string-like text you want to pass.
# latitude = numeric value or string containning a numeric value
# longitude = numeric value or string containning a numeric value

def sendRaw(date, band, value, sensor_id, type_id, longitude, latitude,
comment = None, url = 'http://192.168.45.156/sensores/web/mediciones', 
type = 'json'):

  payload = {"fecha_toma": date, "banda": band, "valor_medido": value,
   "sensor": sensor_id, "tipo": type_id, "comentario": comment,
   "latitud": latitude, "longitud": longitude}
  sendJson(payload)
  return 1
