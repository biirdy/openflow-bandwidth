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
report_port

report_flow - <b> Not implemented </b>

report_switch_ports

report_switch_flows - <b> Not implemented </b>

reset_port

reset_flow - <b> Not implemented </b>

reset_all



