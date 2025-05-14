import subprocess
import defs

def check_uptime(uptime_command, err_updays):
    output = []
    output = defs.printAndAppend("************************", output)
    output = defs.printAndAppend("Start uptime diagnostics", output)
    output = defs.printAndAppend("", output)

    try:
        # uptimeコマンドを実行
        result = subprocess.run(uptime_command, capture_output=True, text=True, shell=True, encoding="utf-8").stdout
        output = defs.printAndAppend(result,output)
    except Exception as e:
        output = defs.printAndAppend(f"error: {e}",output)
        return "\n".join(output), False
    
    if "day" in result:
        # uptimeの値を取得
        days = int(result.split("up")[1].split(",")[0].strip().split()[0])
        if days < err_updays:
            output = defs.printAndAppend(f"Warning: Uptime is less than {err_updays} days", output)
            return "\n".join(output), False
    else:
        output = defs.printAndAppend("Error: Uptime is less than 1 day or format is unexpected", output)
        return "\n".join(output), False

    output = defs.printAndAppend("", output)
    output = defs.printAndAppend("Finished uptime diagnostics", output)
    output = defs.printAndAppend("************************", output)

    return "\n".join(output), True