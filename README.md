OpenFlow Bandwidth
==================
A modification of a the ryu (http://osrg.github.io/ryu/) simple learning switch controller app to report and enforce bandwidth.
Reporting by monotring the maximum passive throughput and enforcing using OpenFlow meters, both on a per port and per flow basis.
The controller runs a JSON-RPC server for interfacing. Procedures shown below. 

## Quick start
Install Ryu

`% pip install ryu`

Pull

`% git pull http://github.com/birrdy/openflow_bandwidth`

Run bandwidth_control_simple_switch_13.py as a Ryu app

`% ryu-manager bandwidth_control_simple_switch_13.py`

By default the RPC server is running on `http://localhost:4000/jsonrpc`

## JSON RPC interface
The JSON-RPC server is a HTTP server.
The following examples would be used to develop a python application using the python-jspnrpc library (https://pypi.python.org/pypi/python-jsonrpc), but procedures can be called using any JSON-RPC method. (I think)

Install 

`% pip install python-jsonrpc`

Import

`import pyjsonrpc`

Connection

`http_client = pyjsonrpc.HttpClient(url = "http://localhost:4000/jsonrpc")`

Procedure calling. 

```
# Direct call
result = http_client.call("<procedure>", arg1, arg2)

# Use the *method* name as *attribute* name
result = http_client.procedure(arg1, arg2)

# Notifcations send messages to the serevr without reply
http_client.notify("<procedure>", arg1, arg2)
```

<h3> Procedures </h3>

<b> report_port </b>

Reports the maximum seen throughput of a specific port on a specific switch.
<br> Returns a `[upload B/s, download B/s]` tuple.

```
--> {"jsonrpc": "2.0", "method": "report_port", "params": [<switch_id>, <port_no>], "id": 1}
<-- {"jsonrpc": "2.0", "result": [<upload B/s>, <download B/s>], "id": 1}
```

<b> report_flow -  Not implemented </b>

Reports the throughout of a specific flow on a specific switch.
<br> Returns a single B/s value.

<br><b> report_switch_ports </b>
<br>Reports the throughput of all ports on a specific switch.

<br><b> report_switch_flows - <b> Not implemented </b>
Reports the througput of all flows on a specific switch.

<br><b> reset_port </b>
Resets the throughput of a specific port. To be recalculated.

<br><b> reset_flow - <b> Not implemented </b>
Resets the throughput of a specific flow. To be recalculated.

<br><b> reset_all </b>
Resets all throughputs on all swtiches under the control of the controller.



