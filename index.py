# index.py

import sys
from routes.frontend import index


app = index.app


##################################################################
import socket    
host = socket.getfqdn()    
addr = socket.gethostbyname(host)
if(addr == '127.0.1.1'):
   app.run(host='localhost', port=8000, debug=True, reloader=True)
##################################################################