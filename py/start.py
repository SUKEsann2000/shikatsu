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
output = defs.printAndAppend("", output)
output = defs.printAndAppend("", output)

import diag_wireguard
#wireguard_command = ["systemctl", "status", "wg-quick@wg0"]
wireguard_command = ["echo", "WireGuard status check"]
wireguard_outputs, wireguard_result = diag_wireguard.check_wireguard(wireguard_command)
output = defs.printAndAppend("", output)
output = defs.printAndAppend("", output)

import diag_ufw
ufw_command = ["sudo", "ufw", "status"]
ufw_ports = [51820, 443, 53]
ufw_outputs, ufw_result = diag_ufw.check_port(ufw_command, ufw_ports)
output = defs.printAndAppend("", output)
output = defs.printAndAppend("", output)

import diag_ntp
ntp_servers = ["0.debian.pool.ntp.org", "1.debian.pool.ntp.org", "2.debian.pool.ntp.org", "3.debian.pool.ntp.org"]
ntp_outputs, ntp_result = diag_ntp.check_ntp_server(ntp_servers)
output = defs.printAndAppend("", output)
output = defs.printAndAppend("", output)

output = defs.printAndAppend("************************", output)
output = defs.printAndAppend("Finished diagnostics", output)
output = defs.printAndAppend("************************", output)