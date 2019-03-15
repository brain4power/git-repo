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

    def process_data(self, data):
        try:
            assert data != ''
            data = data.split()
            assert 1 < len(data) < 5
            if data[0].lower == 'put':
                assert 2 < len(data) < 5
                try:
                    return self._process_put(data[1], data[2], timestamp=data[3])
                except IndexError:
                    return self._process_put(data[1], data[2])
            elif data[0].lower == 'get':
                assert len(data) == 2
                return self._process_get(data[1])
            else:
                raise AssertionError
        except AssertionError:
            return 'error\nwrong command\n\n'

    def _process_get(self, param):
        if param == '*':
            result = 'ok\n'
            for each in self._metrics:
                result += self._make_response_for_get(each)
            return result + '\n'
        elif param in self._metrics:
            return f'ok\n' + self._make_response_for_get(param) + '\n'
        else:
            return 'ok\n\n'

    def _make_response_for_get(self, name):
        response = f'{name} '
        for each in sorted(self._metrics[name]):
            response += f'{each[1]} {each[0]}\n'
        return response

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
        return 'ok\n\n'


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
