import asyncio
import ipaddress
import threading

import util
from client import Client


def parse_ip(ip_str: str):
    ip, port = ip_str.split(':', 2)
    ipaddress.ip_address(ip)
    return str(ip), int(port)


ip, port = util.input_validated(
    "Server IP: ",
    parse_ip,
    parse_ip
)

name = util.input_validated(
    "What is your name?\r\n> ",
    lambda v: 0 < len(v) <= 25,
    error="Please choose a name between 1 and 25 characters long"
)

client = Client(name)


async def main(c: Client):
    await c.connect(ip, port)

    while True:
        msg = util.input_validated(
            "> ",
            lambda v: 0 < len(v) < 250,
            error="Enter a message between 1 and 250 characters"
        )

        await c.send_message(msg)


asyncio.run(main(client))
