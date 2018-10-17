import asyncio
import base64
import json


class Client:
    rx: asyncio.StreamReader
    tx: asyncio.StreamWriter
    name: str

    def __init__(self, name):
        self.name = name

    async def connect(self, server_ip, server_port):
        self.rx, self.tx = await asyncio.open_connection(str(server_ip), server_port)

        await self.send_message(self.name)


    async def send_message(self, msg):
        self.tx.write(base64.b64encode(json.dumps(msg).encode("ascii")))
        self.tx.write(b'\n')
        await self.tx.drain()