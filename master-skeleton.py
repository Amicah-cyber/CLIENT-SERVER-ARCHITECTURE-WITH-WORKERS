from unicodedata import name
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.client import ServerProxy
import sys
import json

#from matplotlib.backend_bases import LocationEvent



workers = {
    'worker-1': ServerProxy("http://localhost:23001/"),
    'worker-2': ServerProxy("http://localhost:23002/")
}
      
def getbylocation(loc1):
    # TODO
    return {
            'error': False,
            'result': []
     }


def getbyname(name):
    # TODO
     return {
        'error': False,
        'result': []
    }

def getbyyear(loc1, year):
    # TODO
    return {
            'error': False,
            'result': []
     }    

def main():
    port = 8000
    #int(sys.argv[1])
    server = SimpleXMLRPCServer(("localhost", port))
    print(f"Listening on port {port}...")

    # TODO: register RPC functions
    server.register_function(getbyname,"name")
    server.register_function(getbylocation)
    #server.register_function(getbyyear,loc1,year)
    server.serve_forever()


if __name__ == '__main__':
    main()