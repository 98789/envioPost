from WSConsumer import  sendRaw
import datetime
from numpy.random import randint

date = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
tag = randint(1,11)
value = ""
for i in range(randint(1,16)):
    for j in range (randint(1,200)):
        value+=str(randint(20000))+" "
    value+=";"
sensor_id = 2
type_id = randint(1,4)
longitude = -72 + randint(-20000,20000)/10000.0
latitude = 7 + randint(-10000,10000)/10000.0
comment = "Automatically generated from python script"

sendRaw(date, tag, value, sensor_id, type_id, longitude, latitude, comment)
