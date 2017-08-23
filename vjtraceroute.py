#!/usr/bin/python


# how to run this script:
# $ sudo python vjtraceroute.py
# $ sudo ./vjtracetroute.py  <-- because path is given in first line

import socket

def vjtraceroute(dest_name):
    dest_addr = socket.gethostbyname(dest_name)
    port      = 33435
    max_hops  = 20
    ttl       = 1
    
    icmp      = socket.getprotobyname('icmp')
    udp       = socket.getprotobyname('udp')

    while True:
        # recv icmp
        recv_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
        recv_socket.bind(("", port))

        # send udp
        send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, udp)
        send_socket.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)
        send_socket.sendto("XYZ", (dest_name, port))

        curr_addr = None
        curr_name = None
        try:
            _, curr_addr = recv_socket.recvfrom(512)
            curr_addr = curr_addr[0]
            try:
                curr_name = socket.gethostbyaddr(curr_addr)[0]
            except socket.error:
                curr_name = curr_addr
        except socket.error:
            pass
        finally:
            send_socket.close()
            recv_socket.close()

        if curr_addr is not None:
            curr_host = "%s (%s)" %(curr_name, curr_addr)
        else:
            curr_host = "* *"

        print "%d\t%s" %(ttl, curr_host)

        ttl += 1

        if curr_addr == dest_addr or ttl > max_hops:
            break


if __name__ == "__main__":
    dst = raw_input("Enter destination to trace: ")
    vjtraceroute(str(dst))
    #vjtraceroute('8.8.8.8')


