import defs

import subprocess

def check_port(command, ports):
    result_flag = True
    output = []
    output = defs.printAndAppend("************************", output)
    output = defs.printAndAppend("Start ufw diagnostics", output)
    output = defs.printAndAppend("", output)

    try:
        # ufwのステータスを取る
        result = subprocess.run(command, capture_output=True, text=True, shell=True, encoding="utf-8")
        output = defs.printAndAppend(result.stdout,output)
        
        output = defs.printAndAppend(f"{'Status':<8} {'Port':<5}",output)
        output = defs.printAndAppend("-" * (8 + 6),output)

        for port in ports:
            # ポートが許可されてるか調べる
            if f"{port}" in result.stdout:
                output = defs.printAndAppend(f"{'Allowed':<8} {port:<6}", output)
            else:
                output = defs.printAndAppend(f"{'Denied':<8} {port:<6}", output)
                result_flag = False
    except Exception as e:
        output = defs.printAndAppend(f"error: {e}",output)
        return "\n".join(output), False
    
    output = defs.printAndAppend("", output)
    output = defs.printAndAppend("Finished ufw diagnostics", output)
    output = defs.printAndAppend("************************", output)

    return "\n".join(output), result_flag