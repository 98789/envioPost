#!/usr/bin/python
# -*- coding: utf-8 -*-
from json import dumps
import requests

# Send data to web service, passing a JSON object as INPUT
def sendJson(payload, url = 'http://192.168.45.156/sensores/web/mediciones', type = 'json'):

  if type == 'json':
    headers = {'content-type': 'application/json'}
  elif type == 'xml':
    headers = {'content-type': 'application/xml'}
  else:
    print "unknown content type"
    return -1

  r = requests.post(url, data=dumps(payload), headers=headers)

  responses = {
  1: '',
  2: 'Los datos han sido almacenados con éxito.',
  3: '',
  4: 'Error, no se encontraron datos o el formato es incorrecto.',
  5: 'Error, los datos contienen valores no válidos.'
  }

  print r.status_code,': ',responses[r.status_code/100]

  return 1

# Send data to web service, passing each value (one by one)
def sendRaw(date, band, value, sensor_id, type_id, comment = None,
url = 'http://192.168.45.156/sensores/web/mediciones', type = 'json'):

  payload = {"fecha_toma": date, "banda": band, "valor_medido": value, "sensor": sensor_id, "tipo": type_id, "comentario": comment}
  sendJson(payload)
  return 1
