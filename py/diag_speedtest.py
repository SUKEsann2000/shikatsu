import sys
import speedtest

def get_speed_test():
    servers = [48463] # IPAのサーバーを選択
    stest = speedtest.Speedtest(secure=True)
    stest.get_servers(servers)
    best = stest.get_best_server()
    return stest, best

import defs
"""
def check_network_speed():
    stest = get_speed_test()
    down_result = stest.download()
    up_result = stest.upload()
    print(str(down_result) + ',' + str(up_result))
"""

def check_network_speed(err_down_mbps, err_up_mbps):
    output = []
    output = defs.printAndAppend("************************", output)
    output = defs.printAndAppend("Start network speed diagnostics", output)
    output = defs.printAndAppend("", output)

    stest, best = get_speed_test()

    output = defs.printAndAppend("************************", output)
    output = defs.printAndAppend(f"Best server: {best['host']} ({best['sponsor']})", output)
    output = defs.printAndAppend(f"Latency(Ping): {best['latency']} ms", output)
    output = defs.printAndAppend(f"Server location: {best['name']}, {best['country']}", output)
    output = defs.printAndAppend(f"Server ID: {best['id']}", output)
    output = defs.printAndAppend("", output)

    output = defs.printAndAppend(f"Error Speed Download: {err_down_mbps} Mbps", output)
    output = defs.printAndAppend(f"Error Speed Upload: {err_up_mbps} Mbps", output)
    output = defs.printAndAppend("************************", output)
    output = defs.printAndAppend("", output)

    down_result = stest.download()
    output = defs.printAndAppend(f"Download speed: {down_result / 1_000_000:.2f} Mbps", output)

    output = defs.printAndAppend("", output)
    up_result = stest.upload()
    output = defs.printAndAppend(f"Upload speed: {up_result / 1_000_000:.2f} Mbps", output)

    output = defs.printAndAppend("", output)

    if down_result < 0 or up_result < 0:
        output = defs.printAndAppend("Error: Speed test failed", output)
        return "\n".join(output), False
    
    if down_result < err_down_mbps or up_result < err_up_mbps:
        output = defs.printAndAppend("Warning: Speed test results are below expected thresholds", output)
        return "\n".join(output), False

    output = defs.printAndAppend("", output)
    output = defs.printAndAppend("Finished network speed diagnostics", output)
    output = defs.printAndAppend("************************", output)
    return "\n".join(output), True