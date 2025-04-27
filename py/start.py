print("************************")
print
print("Start diagstics")
print("************************")
print()
print()

import diag_ping
ping_urls = ["1.1.1.1", "example.com", "google.com"]
ping_outputs, ping_result = diag_ping.check_ping(ping_urls)

print(ping_result)

print()
print()

import diag_wireguard
wireguard_command = ["systemctl", "status", "wg-quick@wg0"]
wireguard_outputs, wireguard_result = diag_wireguard.check_wireguard(wireguard_command)
print()
print()