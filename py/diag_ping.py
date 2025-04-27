import defs

from ping3 import ping

# PING


def check_ping(urls):
    output = []

    output = defs.printAndAppend("************************", output)
    output = defs.printAndAppend("Start pinging",output)
    output = defs.printAndAppend("",output)
    
    max_len = max(len(url) for url in urls)

    output = defs.printAndAppend(f"{'Status':<10} {'URL':<{max_len}} {'Time':>10}",output)
    output = defs.printAndAppend("-" * (10 + max_len + 12),output)

    for url in urls:
        res = ping(url)
        if res is not None and res is not False:
            output = defs.printAndAppend(f"{'Success':<10} {url.ljust(max_len)} {res:>10.4f}",output)
        else:
            output = defs.printAndAppend(f"{'Failed':<10} {url.ljust(max_len)} {'-':>10}",output)
            return "\n".join(output), False

    output = defs.printAndAppend("",output)
    output = defs.printAndAppend("Finished Ping Diagnostics",output)
    output = defs.printAndAppend("************************",output)

    return "\n".join(output), True
