import pyshark

def capture_packets(interface='eth0', count=100):
    capture = pyshark.LiveCapture(interface=interface)
    packets = []
    for i, packet in enumerate(capture.sniff_continuously()):
        try:
            pkt = {
                'src': packet.ip.src,
                'dst': packet.ip.dst,
                'protocol': packet.transport_layer,
                'length': packet.length,
                'info': str(packet)
            }
            packets.append(pkt)
        except AttributeError:
            continue
        if i >= count:
            break
    return packets
