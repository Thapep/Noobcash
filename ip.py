import netifaces
# A function to get the VM's private IP (e.g. 192.168.0.4)
def get_my_ip():
    """
    Find my private IP address
    :return:
    """
    iface = netifaces.ifaddresses('eth1').get(netifaces.AF_INET)
    result = iface[0]["addr"]
    print(result)
    return(result)