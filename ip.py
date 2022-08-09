import os

ip_list = ['8.8.8.8','192.168.0.100','googl.com']
for ip in ip_list:
    response = os.popen(f"ping {ip}").read()
    if "Received = 4" in response:
        print(f"UP {ip} Ping Successful")
    else:
        print(f"DOWN {ip} Ping Unsuccessful")
