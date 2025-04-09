import pyshark
import pandas as pd

def capture_packets(interface='eth0', packet_count=100):
    capture = pyshark.LiveCapture(interface=interface)
    packets = []

    for i, packet in enumerate(capture.sniff_continuously()):
        try:
            pkt = {
                'src': packet.ip.src,
                'dst': packet.ip.dst,
                'protocol': packet.transport_layer,
                'length': int(packet.length),
                'info': str(packet.highest_layer)
            }
            packets.append(pkt)
        except AttributeError:
            continue

        if i >= packet_count:
            break

    df = pd.DataFrame(packets)
    df.to_csv("data/preprocessed/packets.csv", index=False)
    print(f"[+] Saved {len(df)} packets to CSV.")
