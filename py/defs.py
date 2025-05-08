def printAndAppend(message, output):
    #print(message)
    output.append(message)
    return output

def format_data_as_table(data: dict) -> str:
    lines = []
    max_key_length = max(len(key) for key in data.keys())
    for key, value in data.items():
        lines.append(f"{key.ljust(max_key_length)} : {value}")
    return "\n".join(lines)
