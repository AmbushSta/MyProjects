"""
   Given a list of ipv4 or ipv6 addresses, returns a list replacing
   the address in the same index with the corresponding string.
   Author: Michael Cowie
"""

def checkIPs(ip_array):
    outputs = []
    for ip in ip_array:
        if isIPV6(ip):
            outputs.append("IPv6")
        elif isIPV4(ip):
            outputs.append("IPv4")
        else:
            outputs.append("Neither")
    return outputs
            
def isIPV6(ip):
    for x in ip.split(":"):
        try:
            if int(x, 16) >= 0xffff or int(x, 16) < 0:
                return False
        except:
            return False
    return True

def isIPV4(ip):
    for value in ip.split("."):
        try:
            if int(value) not in range(0, 256):
                return False
        except:
            return False
    return True

"""
   Example:
   print(checkIPs(["172.16.254.1", "2001:0DB8:AC10:FE01", "This line has junk text."])) ->
   ['IPv4', 'IPv6', 'Neither']
"""
