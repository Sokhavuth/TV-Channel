# index.py

from bottle import static_file, get
from routes.frontend import index


app = index.app

@app.get('/static/<filepath:path>')
def staticFile(filepath):
    return static_file(filepath, root="public")


###################################################################
import socket
host = socket.getfqdn()    
addr = socket.gethostbyname(host)
if(addr == '127.0.1.1'):
    app.run(host='localhost', port=8000, debug=True, reloader=True)

###################################################################