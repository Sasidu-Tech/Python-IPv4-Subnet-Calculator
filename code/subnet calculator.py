import ipaddress

print("=" * 35)
print("IPV4 SUBNET CACULATOR")
print("=" * 35)

try:
    ip_input = input("Enter IP address with CIRD (e.g.192.168.1.10/24): ")

    interface = ipaddress.ip_interface(ip_input)
    network = interface.network

    print("\n---Network Information---")
    print("ip Address    : ",interface.ip)
    print("Subnet mask   : ",network.netmask)
    print("Network Address  : ",network.network_address)
    print("Broadcast Address   : ",network.broadcast_address)
    print("CIDR Prefix   : ",network.prefixlen)
    print("Total Address   : ",network.num_addresses)

    if (network.num_addresses > 2):
        print("usable Host Ips :", network.num_addresses - 2)
    else:
        print("Usable Host Ips : Depends on network type")    

except ValueError:
    print("Invalid IP address or CIDR prefix!")    
