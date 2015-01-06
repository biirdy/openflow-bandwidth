OpenFlow Bandwidth
==================
A modification of a the ryu simple learning switch controller app to report and enforce bandwidth.
Reporting by monotring the maximum passive throughput and enforcing using OpenFlow meters, both on a per port and per flow basis.
The controller runs a JSON-RPC server for interfacing. Procedures shown below. 

## Quick start
Install Ryu

`% pip install ryu`

Pull

`% git pull http://github.com/birrdy/openflow_bandwidth`

Run bandwidth_control_simple_switch_13.py as a Ryu app

`% ryu-manager bandwidth_control_simple_switch_13.py`

## JSON RPC interface
The JSON-RPC server is a Http server.
The following examples would be used to develop a python application but procedures can be called using any JSON-RPC method.

Connection
`http_client = pyjsonrpc.HttpClient(url = "http://localhost:4000/jsonrpc")`

<b> report_port

<b> report_flow -  Not implemented </b>

<b> report_switch_ports

<b> report_switch_flows - <b> Not implemented </b>

<b> reset_port

<b> reset_flow - <b> Not implemented </b>

<b> reset_all



