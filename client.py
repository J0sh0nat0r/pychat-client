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

        self.read_task = asyncio.create_task(self.read_loop())

    async def send_message(self, msg):
        self.tx.write(base64.b64encode(json.dumps(msg).encode("ascii")))
        self.tx.write(b'\n')
        await self.tx.drain()

    async def read_loop(self):
        msg = await self.read_message()

        while msg is not None:
            if msg.type == "message":
                print(msg.author_name + ": " + msg.text)

            msg = await self.read_message()

    async def read_message(self):
        try:
            line = await self.rx.readline()

            # EOF, client disconnected
            if len(line) == 0:
                return None

            return json.loads(base64.b64decode(line))
        except:
            return None
