#!/usr/bin/python
from json import dumps
import requests

def send(payload, url='http://radiogis.uis.edu.co/sensores/web/medidas',
         type='json'):
    """Send formatted data to a web service"""

    types = {'json':'application/json','xml':'application/xml'}

    try:
        headers = {'content-type': types[type]}
    except KeyError:
        raise Exception("unknown content type %s" % type)
        return 0

    r = requests.post(url, data=dumps(payload), headers=headers)

    print(r.json())
    return 1


# date: String containing a date formatted as dd/mm/yyyy hh:mm:ss.
# tag: Any aditional information you consider necessary, such as band.
# value: A number (for single sensors) or a matrix stored in a string
#        (using semicolons for rows and tabs for columns).
# sensor_id: check current valid ids and add new ones at: 
#            http://radiogis.uis.edu.co/sensores/web/sensor.
# type_id: 1, 2 or 3, as of 05.04.15 this is a dummy column (it probably makes no sense).
# comment: Optional, any string-like text you want to pass.
# lat: numeric value or string containning a numeric value
# long: numeric value or string containning a numeric value

def send_raw(date, value, sensor_id, type_id, long, lat, comment=None,
             url='http://radiogis.uis.edu.co/sensores/web/medidas',
             type='json', tag=None):
    """Send raw data to a web service"""

    payload = {"fecha_toma": date, "etiqueta": tag, "valor_medido": value,
               "sensor": sensor_id, "tipo": type_id, "comentario": comment,
               "latitud": lat, "longitud": long}
    send(payload, url, type)
    return 1
