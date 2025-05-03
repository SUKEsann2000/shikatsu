import defs

import ntplib
from time import ctime

def check_ntp_server(servers):
    failCount = 0

    output = []
    error = []
    output = defs.printAndAppend("************************", output)
    output = defs.printAndAppend("Start NTP diagnostics", output)
    output = defs.printAndAppend("", output)

    max_len = max(len(server) for server in servers) + 3

    output = defs.printAndAppend(f"{'Status':<10} {'Server':<{max_len}} {'Time':<30}", output)
    output = defs.printAndAppend("-" * (10 + 20 + 30), output)

    client = ntplib.NTPClient()

    for server in servers:
        try:
            response = client.request(server)
            output = defs.printAndAppend(f"{'Success':<10} {server:<{max_len}} {ctime(response.tx_time):<30}", output)
        except Exception as e:
            output = defs.printAndAppend(f"{'Failed':<10} {server:<{max_len}} {'-':<30}", output)
            error.append(f"Error: {e}")
            failCount += 1

    output = defs.printAndAppend("", output)
    output += error
    output = defs.printAndAppend("\n".join(error),output)

    output = defs.printAndAppend("", output)
    output = defs.printAndAppend("Finished NTP diagnostics", output)
    output = defs.printAndAppend("************************", output)
    if failCount == len(servers):
        return "\n".join(output), False
    return "\n".join(output), True