# envioPost
# by JAMM

Open command line and navigate to the current (this) directory, then 
type "python" (without quotes) and, once there, import the downloaded 
script:

from consumer import *
or
from sendScript import *

(depending on whether you want lat/long support or not)

call the functions passing the required values as a formatted object 
(send) or single, raw (send_raw) in the specified order.

You will be notified about the success or failure of the process once 
it is concluded. To confirm that the data is being added, go to 
http://radiogis.uis.edu.co/sensores/web/medida, verify the sent data 
and the "fecha registro" column.
