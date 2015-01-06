import pyjsonrpc

class rcp_server:
	def __init__(self):
		self._running = True

	def terminate(self):
		self._running = False

	def run(self, num, max_throughput):
		http_server = pyjsonrpc.ThreadingHttpServer(server_address = ('localhost', 4000),RequestHandlerClass = RequestHandler)
		http_server.max_throughput = max_throughput
		http_server.serve_forever()

class RequestHandler(pyjsonrpc.HttpRequestHandler):
	@pyjsonrpc.rpcmethod
	def report_port(self, switch, port):
		return self.server.max_throughput[switch][port]

	@pyjsonrpc.rpcmethod
	def reset_port(self, switch, port):
		slef.serevr.max_throughput[switch][port] = [0,0]

	@pyjsonrpc.rpcmethod
	def reset_all(self, switch, port):
		slef.serevr.max_throughput = {}

	@pyjsonrpc.rpcmethod
	def report_all(self, switch, port):
		return slef.serevr.max_throughput










