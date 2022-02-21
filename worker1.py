from os import name
from tokenize import group
from xmlrpc.server import SimpleXMLRPCServer
import sys
import json

from rx import if_then
from webob import year

# Storage of data
with open("data-am.json", "r") as data_file:
    data_table = json.load(data_file)



def load_data(group):
    # TODO load data based which portion it handles (am or nz)
    
    return(data_table)


def printdic():
    with open("data-am.json", "r") as data_file:
        x=json.load(data_file)
        dic1 = x['john']
        m=dic1['name']
    return(m)


def getbyname(name):
    # TODO
    #   data_table = json.load(data_file)
    x=data_table[name]
    name =x['name']
    return (name)

def getbylocation(location):
    # TODO
    
        #data_table = json.load(data_file)
    for x in data_table:
        for m in x:
            print(m)
            if m == location:
                print(m) 
    print(location)
    return (location)

def getbyyear(location, year):
    # TODO
     for x in data_table:
        for m in x:
            print(m)
            if m == location:
                print(m)
            if m == year:
                print(m) 
        return (location,year)

def main():
    #if len(sys.argv) < 2:
     #   print('Usage: worker.py <port> <group: am or nz>')
     #   sys.exit(0)

    port = 23001
    #int(sys.argv[1]) #argument 1
    server = SimpleXMLRPCServer(("localhost", port))
    print(f"Listening on port {port}...")

    # TODO register RPC functions
    server.register_function(printdic)
    server.register_function(load_data)
    server.register_function(getbyname)
    server.register_function(getbylocation)
    server.register_function(getbyyear)
    server.serve_forever()

if __name__ == '__main__':
    main()