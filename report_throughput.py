#!/usr/bin/python

import pyjsonrpc
import sys, getopt

def __init__(self):
	http_client = None


#print http_client.call("add", 1, 2)
# Result: 3

# It is also possible to use the *method* name as *attribute* name.
#print http_client.call("report_port", 1, 3)



# Notifications send messages to the server, without response.
#http_client.notify("add", 3, 4)

def main(argv):
	http_client = pyjsonrpc.HttpClient(url = "http://localhost:4000/jsonrpc")

	if http_client == None:
		print 'Could not connect to rcp server'
		sys.exit()

	usage = "usage: \nreport_throughput.py -a\t\t\t\tall ports all switchs\nreport_throughput.py -s <switch_id>\t\tall ports on <switch_id>\nreport_throughput.py -s <seitch_id> -p <port_no> \tportn <port_no> on switch <switch_id>"

	al = False
	switch = None
	port = None				

	try:
		opts, args = getopt.getopt(argv,"has:p:",[])
	except getopt.GetoptError:
		print usage
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-a':
			al = True
		elif opt == '-s':
			switch = arg
		elif opt == '-p':
			port = arg
		else:
			print usage
			sys.exit(2)

	if al == True:
		print 'all' 
	elif switch is not None:
		print 'all from switch'
	elif switch is not None:
		print 'port on switch'
	else:
		print usage


if __name__== "__main__":
	main(sys.argv[1:])