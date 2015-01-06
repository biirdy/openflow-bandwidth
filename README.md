OpenFlow Bandwidth
==================
A modification of a the ryu simple learning switch controller app to report and enforce bandwidth.
Reporting by monotring the maximum passive throughput and enforcing using OpenFlow meters, both on a per port and per flow basis.
The controller runs a JSON-RPC server for interfacing. Procedures shown below. 

## Quick start
Install Ryu 
`% pip install ryu`



## JSON RPC interface



