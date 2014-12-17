from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import CONFIG_DISPATCHER, MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_3
from ryu.lib.packet import packet
from ryu.lib.packet import ethernet
from PacketOutLoop import *
from Data import *
from threading import *

class PacketOut(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]

    def __init__(self, *args, **kwargs):
        super(PacketOut, self).__init__(*args, **kwargs)
        self.datapathdict = {}
        self.packet_out_loop = PacketOutLoop()
        self.pollingThread=Thread(target=self.packet_out_loop.run,args=(1,self.datapathdict))
        self.pollingThread.start()

    @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
    def _packet_in_handler(self, ev):
    	msg = ev.msg
        datapath = msg.datapath
        pkt = packet.Packet(msg.data)
        pkt_ethernet = pkt.get_protocol(ethernet.ethernet)
        #pkt_string = pkt.get_protocol(Data)

        self.logger.info("pkt:%s", pkt)

        #self.logger.info("eth:%s", pkt_ethernet)
        #self.logger.info("data%s", pkt_string)
        #self.logger.info("datapath:%s buffer_id:%s data:%s", datapath.id, msg.buffer_id, msg.data)

    	#Add new switches for polling
        self.datapathdict[datapath.id]=datapath

        