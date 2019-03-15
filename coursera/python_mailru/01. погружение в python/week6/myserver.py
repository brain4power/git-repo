import asyncio
import time


class ClientServerProtocol(asyncio.Protocol):
    def __init__(self):
        self._metrics = {}

    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        resp = self.process_data(data.decode())
        self.transport.write(resp.encode())

    def process_data(self, resp):
        try:
            assert resp != ''
            resp = resp.split()
            assert 1 < len(resp) < 5
            if resp[0].lower == 'put':
                assert 2 < len(resp) < 5
                try:
                    return self._process_put(resp[1], resp[2], timestamp=resp[3])
                except IndexError:
                    return self._process_put(resp[1], resp[2])
            elif resp[0].lower == 'get':
                return self._process_get()
            else:
                raise AssertionError
        except AssertionError:
            return 'error\nwrong command\n\n'

    def _process_get(self):
        # упорядочивать по timestamp
        pass

    def _process_put(self, name, value, timestamp=str(int(time.time()))):
        if name in self._metrics:
            timestamp_in_metrics_name = False
            for idx, element in enumerate(self._metrics[name]):
                if timestamp in element:
                    self._metrics[name][idx] = (timestamp, value)
                    timestamp_in_metrics_name = True
                    break
            if not timestamp_in_metrics_name:
                self._metrics[name].append((timestamp, value))
        else:
            self._metrics[name] = [(timestamp, value)]


def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(
        ClientServerProtocol,
        host, port
    )
    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()

