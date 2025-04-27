from ping3 import ping

# PING

output = []

def check_ping(urls):

    printAndAppend("************************")
    printAndAppend("Start pinging")
    printAndAppend("")
    
    max_len = max(len(url) for url in urls)

    printAndAppend(f"{'Status':<10} {'URL':<{max_len}} {'Time':>10}")
    printAndAppend("-" * (10 + max_len + 10))

    for url in urls:
        res = ping(url)
        if res is not None and res is not False:
            printAndAppend(f"{'Success':<10} {url.ljust(max_len)} {res:>10.4f}")
        else:
            error_message = f"Failed to ping {url}"
            printAndAppend(f"{'Failed':<10} {url.ljust(max_len)} {'-':>10}")
            return "\n".join(output), False

    printAndAppend("")
    printAndAppend("finished pinging")
    printAndAppend("************************")

    return "\n".join(output), True

def printAndAppend(message):
    print(message)
    output.append(message)