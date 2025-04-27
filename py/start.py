import defs

output = []

output = defs.printAndAppend("************************", output)
output = defs.printAndAppend("Start diagstics", output)
output = defs.printAndAppend("************************", output)
output = defs.printAndAppend("", output)
output = defs.printAndAppend("", output)

import diag_ping
ping_urls = ["1.1.1.1", "example.com", "google.com", "sukesann2000.com"]
ping_outputs, ping_result = diag_ping.check_ping(ping_urls)
output = defs.printAndAppend(ping_outputs, output)
output = defs.printAndAppend("", output)
output = defs.printAndAppend("", output)

import diag_wireguard
#wireguard_command = ["systemctl", "status", "wg-quick@wg0"]
wireguard_command = ["echo", "WireGuard status check"]
wireguard_outputs, wireguard_result = diag_wireguard.check_wireguard(wireguard_command)
output = defs.printAndAppend(wireguard_outputs, output)
output = defs.printAndAppend("", output)
output = defs.printAndAppend("", output)

import diag_ufw
ufw_command = ["sudo", "ufw", "status"]
ufw_ports = [51820, 443, 53]
ufw_outputs, ufw_result = diag_ufw.check_port(ufw_command, ufw_ports)
output = defs.printAndAppend(ufw_outputs, output)
output = defs.printAndAppend("", output)
output = defs.printAndAppend("", output)

import diag_ntp
ntp_servers = ["0.debian.pool.ntp.org", "1.debian.pool.ntp.org", "2.debian.pool.ntp.org", "3.debian.pool.ntp.org"]
ntp_outputs, ntp_result = diag_ntp.check_ntp_server(ntp_servers)
output = defs.printAndAppend(ntp_outputs, output)
output = defs.printAndAppend("", output)
output = defs.printAndAppend("", output)

output = defs.printAndAppend("************************", output)
output = defs.printAndAppend("Finished diagnostics", output)
output = defs.printAndAppend("************************", output)


flattened_output = []
for item in output:
    if isinstance(item, list):
        flattened_output.extend(item)
    else:
        flattened_output.append(item)

print("\n".join(flattened_output))

import requests
import json

# Send data to Google Apps Script
url = "https://script.google.com/macros/s/AKfycbyrB1Ng4-LVaYrgrkoZptbDKmB4F6HDc9X2vlYGABUEo4udtb89bNtvucq0-opiOI3S/exec"  # GASのURLを入力
headers = {
    "Content-Type": "application/json"
}

data = {
    "output": flattened_output
}

response = requests.post(url, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    print("Successed to send data")
else:
    print(f"Failed to send data: {response.status_code}")
