import socket
import struct
import binascii

class Udphdr:
    def __init__(self, sport, dport, length, checksum):
        self.source_port = sport
        self.destination_port = dport
        self.udpp_length = length
        self.checksum = checksum

    def pack_Udphdr(self):
        packed = b''
        packed += struct.pack('!H', self.source_port)
        packed += struct.pack('!H', self.destination_port)
        packed += struct.pack('!H', self.udpp_length)
        packed += struct.pack('!H', self.checksum)
        return packed

    def unpack_Udphdr(buffer):
        unpacked = struct.unpack('!HHHH', buffer[:8])
        return unpacked

    def getSPort(unpacked_Udpheader):
        return unpacked_Udpheader[0]

    def getDPort(unpacked_Udpheader):
        return unpacked_Udpheader[1]

    def getLength(unpacked_Udpheader):
        return unpacked_Udpheader[2]

    def getChecksum(unpacked_Udpheader):
        return unpacked_Udpheader[3]
        
        
Udp = Udphdr(5555, 80, 1000, 0xFFFF)
packed_Udphdr = Udp.pack_Udphdr()
print(binascii.b2a_hex(packed_Udphdr))

unpacked_Udphdr = Udphdr.unpack_Udphdr(packed_Udphdr)
print(unpacked_Udphdr)
print('Source Port:{} Destination Port:{} Length:{} Checksum:{}' 
.format(Udphdr.getSPort(unpacked_Udphdr), Udphdr.getDPort(unpacked_Udphdr), 
Udphdr.getLength(unpacked_Udphdr), Udphdr.getChecksum(unpacked_Udphdr)))