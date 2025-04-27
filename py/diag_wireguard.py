# WireGuardのstatusの監視

import defs

import subprocess

def check_wireguard(command):
    output = []

    output = defs.printAndAppend("************************", output)
    output = defs.printAndAppend("Start WireGuard diagnostics", output)
    output = defs.printAndAppend("", output)
    output = defs.printAndAppend("", output)

    # Run command and capture the output
    result = subprocess.run(command, capture_output=True, text=True, shell=True)

    output = defs.printAndAppend("*********************", output)
    output = defs.printAndAppend("Command   " + " ".join(command), output)
    output = defs.printAndAppend("*********************", output)
    output = defs.printAndAppend("", output)

    output = defs.printAndAppend("*********************", output)
    output = defs.printAndAppend("Output", output)
    output = defs.printAndAppend("*********************", output)

    output = defs.printAndAppend(result.stdout, output)

    if result.returncode != 0:
        output = defs.printAndAppend("Error:", result.stderr, output)
        return "\n".join(output), False
    
    output = defs.printAndAppend("", output)
    output = defs.printAndAppend("Finished WireGuard diagnostics", output)
    output = defs.printAndAppend("************************", output)
    return "\n".join(output), True