import defs

output = []

output = defs.printAndAppend("************************", output)
output = defs.printAndAppend("Start diagstics", output)
output = defs.printAndAppend("************************", output)
output = defs.printAndAppend("", output)
output = defs.printAndAppend("", output)

import diag_ping
ping_urls = ["1.1.1.1", "example.com", "google.com", "sukesann2000.duckdns.org"]
ping_outputs, ping_result = diag_ping.check_ping(ping_urls)
output = defs.printAndAppend(ping_outputs, output)
output = defs.printAndAppend("", output)
output = defs.printAndAppend("", output)

import diag_wireguard
wireguard_ui_command = "systemctl status wg-quick@wg0"
#wireguard_ui_command = ["echo", "WireGuard status check"]
wireguard_code_command = "systemctl is-active --quiet wg-quick@wg0"
#wireguard_code_command = ["echo", "WireGuard code check"]
wireguard_outputs, wireguard_result = diag_wireguard.check_wireguard(wireguard_ui_command, wireguard_code_command)
output = defs.printAndAppend(wireguard_outputs, output)
output = defs.printAndAppend(wireguard_result, output)
output = defs.printAndAppend("", output)
output = defs.printAndAppend("", output)

import diag_ufw
ufw_command = "sudo ufw status"
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
    str_item = str(item)
    if isinstance(str_item, list):
        flattened_output.extend(str_item)
    else:
        flattened_output.append(str_item)

print("\n".join(flattened_output))

import requests
import json
import datetime

data_timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Send data to Google Apps Script
url = "https://script.google.com/macros/s/AKfycbzUhMzXhE5zjCoDZDCyN3AK8d1tzgCxA9dLV6Qs0CZeVB5nTNLFKociWJoYlwd2ma10/exec"
headers = {
    "Content-Type": "application/json"
}

data = {
    "timestamp": str(data_timestamp),
    "output": flattened_output,
    "ping_result": str(ping_result),
    "wireguard_result": str(wireguard_result),
    "ufw_result": str(ufw_result),
    "ntp_result": str(ntp_result),
    "speedtest_result": str(speedtest_result)
}

response = requests.post(url, headers=headers, data=json.dumps(data))
if response.status_code == 200:
    print("Successed to send data")
else:
    print(f"Failed to send data: {response.status_code}")