# Edit as needed.
# Only mandatory fields included in this template,
# for optional fields check consumer.py


import consumer


user = "user"
password = "password"
URL = "http://example.com/data"
URL_login = "http://example.com/login"

# Using send

data = {"fecha_toma": "DD/MM/YYYY hh:mm:ss", "valor_medido": <valor>, 
        "sensor": <sensor_id>, "tipo": <tipo_id>, "latitud": +/-xx.xxxxxx, 
        "longitud": +/-xx.xxxxxx, "campanya":  <campanya_id>}

consumer.send(data, URL, URL_login, user, password)

# Using send_raw

fecha_toma = "DD/MM/YYYY hh:mm:ss"
valor_medido = <valor>
sensor = <sensor_id>
tipo = <tipo_id>
latitud = +/-xx.xxxxxx
longitud = +/-xx.xxxxxx
campanya =  <campanya_id>

consumer.send(fecha_toma, valor_medido, sensor, tipo, longitud, latitud, URL, URL_login, user, password)
