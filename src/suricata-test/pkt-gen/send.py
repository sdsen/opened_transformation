from scapy.all import *
import socket

#dst_ip = "127.0.0.1"
dst_ip = "40.0.2.2"
#src_ip = "127.0.0.1"
src_ip = "40.0.1.2"
src_port = 20000
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((src_ip, src_port))
    p = IP(dst=dst_ip,src=src_ip)/UDP(sport=src_port,dport=80)/Raw("Hello world3!")
    #s.connect((src_ip,80))
    s.sendto(bytes(p),(dst_ip, 80))
    print("[+] Request Sent!")
except Exception as e:
    raise e
