import xmlrpc.client
import sys

master_port = 23002
#group = sys.argv[1]#(sys.argv[1])
with xmlrpc.client.ServerProxy(f"http://localhost:{master_port}/") as proxy:
    name = 'rakin'
    print(f'Client => Asking for person with {name}')
    try:
        result = proxy.getbyname(name)
        print(result)
    except xmlrpc.client.Fault as err:
        print("A fault occurred")
        print("Fault code: %d" % err.faultCode)
        print("Fault string: %s" % err.faultString)
    print()

    location = 'Saint Louis'
    print(f'Client => Asking for person lived at {location}')
    result = proxy.getbylocation(location)
    print(result)
    print()

    location = 'Los Angeles'
    year = 2002
    print(f'Client => Asking for person lived in {location} in {year}')
    result = proxy.getbyyear(location, year)  
    print(result)
    print()