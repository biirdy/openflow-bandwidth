# coding: utf-8

import pyjsonrpc
import json

class rcp_server:
	def __init__(self):
		self._running = True

	def terminate(self):
		self._running = False

	def run(self, num, max_throughput, meter_mod):
		http_server = pyjsonrpc.ThreadingHttpServer(server_address = ('localhost', 4000),RequestHandlerClass = RequestHandler)
		http_server.max_throughput = max_throughput
		http_server.meter_mod = meter_mod
		http_server.serve_forever()

class RequestHandler(pyjsonrpc.HttpRequestHandler):
	@pyjsonrpc.rpcmethod
	def report_port(self, switch, port):
		return json.dumps(self.server.max_throughput[int(switch)][int(port)])

	@pyjsonrpc.rpcmethod
	def report_switch_ports(self, switch):
		return json.deumps(self.server.max_throughput[int(switch)])

	@pyjsonrpc.rpcmethod
	def report_all_ports(self):
		return json.dumps(self.server.max_throughput)

	@pyjsonrpc.rpcmethod
	def reset_port(self, switch, port):
		self.server.max_throughput[int(switch)][int(port)] = [0,0]

	@pyjsonrpc.rpcmethod
	def reset_switch_port(self, switch):
		self.server.max_throughput[int(switch)] = {}

	@pyjsonrpc.rpcmethod
	def enforce_port_outbound(self, switch, port, speed):
		self.server.meter_mod(int(switch), int(port), int(speed))












