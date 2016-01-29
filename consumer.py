#!/usr/bin/python
from bs4 import BeautifulSoup
import json
import requests


def get_token(session, URL):
    """Retrieve csrf token URL"""

    login_page = BeautifulSoup(session.get(URL).content)
    login_page.find(attrs={"name":"csrf-token"}).get("content")
    token = login_page.find(attrs={"name":"csrf-token"}).get("content")

    return token

def authenticate(user, password, URL):
    """log in to URL"""

    session = requests.Session()
    headers = {'User-Agent': 'Mozilla/5.0'}

    token = get_token(session, URL)

    payload = {'login-form[login]':user,'login-form[password]':password, '_csrf': token}

    resp = session.post(URL, data=payload, headers=headers)

    if resp.url == URL:
        raise Exception("Error authenticating")
        return 0

    return session


def send(payload, URL, login_URL, user, password, data_format='json'):
    """Send formatted data to a web service"""

    types = {'json':'application/json','xml':'application/xml'}

    try:
        headers = {'content-type': types[data_format]}
    except KeyError:
        raise Exception("unknown content type %s" % data_format)
        return 0

    session = authenticate(user, password, login_URL)
    if session:
        payload['_csrf'] = get_token(session, URL)
        resp = session.post(URL, data=json.dumps(payload), headers=headers)
        print(resp.text)
    else:
        return 0

    return 1


def send_raw(date, value, sensor_id, type_id, lgt, lat, URL, login_URL,
             user, password, comment=None, tag=None, data_format='json'):
    """Send raw data to a web service"""

    payload = {"fecha_toma": date, "etiqueta": tag, "valor_medido": value,
               "sensor": sensor_id, "tipo": type_id, "comentario": comment,
               "latitud": lat, "longitud": lgt}
    send(payload, URL, login_URL, user, password, data_format)

    return 1
