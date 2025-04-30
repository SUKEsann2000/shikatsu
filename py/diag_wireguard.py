# WireGuardのstatusの監視

import defs

import subprocess

def check_wireguard(ui_command, code_command):
    output = []

    output = defs.printAndAppend("************************", output)
    output = defs.printAndAppend("Start WireGuard diagnostics", output)
    output = defs.printAndAppend("", output)
    output = defs.printAndAppend("", output)

    # Run command and capture the output
    ui_result = subprocess.run(ui_command, capture_output=True, text=True, shell=True)

    output = defs.printAndAppend("*********************", output)
    output = defs.printAndAppend("UI Command   " + " ".join(ui_command), output)
    output = defs.printAndAppend("*********************", output)
    output = defs.printAndAppend("", output)

    output = defs.printAndAppend("*********************", output)
    output = defs.printAndAppend("Output", output)
    output = defs.printAndAppend("*********************", output)

    output = defs.printAndAppend(ui_result.stdout, output)
    output = defs.printAndAppend("", output)
    
    code_result = subprocess.run(code_command, capture_output=True, text=True, shell=True)

    output = defs.printAndAppend("**********************", output)
    output = defs.printAndAppend("Code Command   " + " ".join(code_command), output)
    output = defs.printAndAppend("**********************", output)
    output = defs.printAndAppend("", output)
    
    output = defs.printAndAppend("**********************", output)
    output = defs.printAndAppend("Output", output)
    output = defs.printAndAppend("**********************", output)

    output = defs.printAndAppend(code_result.stdout, output)
    output = defs.printAndAppend("", output)

    if ui_result.returncode != 0:
        output = defs.printAndAppend("Error:" + ui_result.stderr, output)
        return "\n".join(output), False
    
    if code_result.returncode != 0:
        output = defs.printAndAppend("Failed:", code_result.stderr, output)
        return "\n".join(output), False

    output = defs.printAndAppend("", output)
    output = defs.printAndAppend("Finished WireGuard diagnostics", output)
    output = defs.printAndAppend("************************", output)
    return "\n".join(output), True