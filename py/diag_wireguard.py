# WireGuardのstatusの監視

import subprocess

output = []

def check_wireguard(command):
    printAndAppend("************************")
    printAndAppend("Start WireGuard diagnostics")
    printAndAppend("")

    # Run command and capture the output
    result = subprocess.run(command, capture_output=True, text=True)

    printAndAppend("Output")
    printAndAppend("")

    printAndAppend(result.stdout)

    if result.returncode != 0:
        printAndAppend("Error:", result.stderr)
        return "\n".join(output), False
    
    return "\n".join(output), True

def printAndAppend(message):
    print(message)
    output.append(message)