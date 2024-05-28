from scapy.all import *

def packet_callback(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = packet[IP].proto

        print(f"Source IP: {src_ip}, Destination IP: {dst_ip}, Protocol: {proto}")

        if TCP in packet:
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
            print(f"Source Port: {src_port}, Destination Port: {dst_port}")

        if UDP in packet:
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
            print(f"Source Port: {src_port}, Destination Port: {dst_port}")

        if Raw in packet:
            payload = packet[Raw].load
            print(f"Payload: {payload}")

# Start sniffing packets on the network interface
sniff(prn=packet_callback, store=0)
