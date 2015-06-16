from consumer import  send_raw
import datetime
from numpy.random import randint

date = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
tag = randint(1,11)
limit_i = randint(1,201)
limit_j = randint(1,17)
value = ';'.join(' '.join(str(randint(20000)) for j in range(limit_j)) for i in range(limit_i))
value = value[0:-1]
sensor_id = 2
type_id = randint(1,4)
long = -72 + randint(-20000,20000)/10000.0
lat = 7 + randint(-10000,10000)/10000.0
comment = "Automatically generated from python script"

send_raw(date, value, sensor_id, type_id, long, lat, comment, tag = tag)
