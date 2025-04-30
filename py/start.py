import defs

output = []

output = defs.printAndAppend("************************", output)
output = defs.printAndAppend("Start diagstics", output)
output = defs.printAndAppend("************************", output)
output = defs.printAndAppend("", output)
output = defs.printAndAppend("", output)

import diag_ping
ping_urls = ["1.1.1.1", "example.com", "google.com"]
ping_outputs, ping_result = diag_ping.check_ping(ping_urls)
output = defs.printAndAppend(ping_outputs, output)
output = defs.printAndAppend("", output)
output = defs.printAndAppend("", output)

import diag_wireguard
wireguard_ui_command = ["systemctl", "status", "wg-quick@wg0"]
#wireguard_ui_command = ["echo", "WireGuard status check"]
wireguard_code_command = ["systemctl", "is-active", "--quiet", "wg-quick@wg0"]
#wireguard_code_command = ["echo", "WireGuard code check"]
wireguard_outputs, wireguard_result = diag_wireguard.check_wireguard(wireguard_ui_command, wireguard_code_command)
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

import diag_speedtest
speedtest_err_down_mbps = 20
speedtest_err_up_mbps = 30
speedtest_outputs, speedtest_result = diag_speedtest.check_network_speed(speedtest_err_down_mbps, speedtest_err_up_mbps)
output = defs.printAndAppend(speedtest_outputs, output)
output = defs.printAndAppend("", output)
output = defs.printAndAppend("", output)

output = defs.printAndAppend("************************", output)
output = defs.printAndAppend("Finished diagnostics", output)
output = defs.printAndAppend("************************", output)
output = defs.printAndAppend("", output)
output = defs.printAndAppend("", output)
output = defs.printAndAppend("", output)


flattened_output = []
for item in output:
    if isinstance(item, list):
        flattened_output.extend(item)
    else:
        flattened_output.append(item)

print("\n".join(flattened_output))

import requests
import json
import datetime

data_timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Send data to Google Apps Script
url = "https://script.google.com/macros/s/AKfycbzUYBngBTeGwhot8iVA1yEwV4FufIaZb22KQGntT_m9nKXNdJNsJkWHx7Y0R2sh2nAd/exec"
headers = {
    "Content-Type": "application/json"
}

data = {
    "timestamp": data_timestamp,
    "output": flattened_output,
    "ping_result": ping_result,
    "wireguard_result": wireguard_result,
    "ufw_result": ufw_result,
    "ntp_result": ntp_result,
    "speedtest_result": speedtest_result
}

response = requests.post(url, headers=headers, data=json.dumps(data))
if response.status_code == 200:
    print("Successed to send data")
else:
    print(f"Failed to send data: {response.status_code}")