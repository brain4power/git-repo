import socket

"""класс Client, в котором будет инкапсулировано соединение с сервером, 
клиентский сокет и методы для получения и отправки метрик на сервер. 
В конструктор класса Client должна передаваться адресная пара хост и порт, 
а также необязательный аргумент timeout (timeout=None по умолчанию). 
У класса Client должно быть 2 метода: put и get, соответствующих протоколу выше.
client = Client("127.0.0.1", 8888, timeout=15)

client.put("palm.cpu", 0.5, timestamp=1150864247)
client.put("palm.cpu", 2.0, timestamp=1150864248)
client.put("palm.cpu", 0.5, timestamp=1150864248)

client.put("eardrum.cpu", 3, timestamp=1150864250)
client.put("eardrum.cpu", 4, timestamp=1150864251)
client.put("eardrum.memory", 4200000)

print(client.get("*"))
"""

# TODO сделать обработку времени ответа сервера
class Client:
    def __init__(self, host, port, timeout=None):
        try:
            self.sock = socket.create_connection((host, port), timeout)
        except:
            raise ClientError

    def put(self, key, value, timestamp):
        self.sock.sendall(f'put {key} {value} {timestamp}\n'.encode())
        data = self.sock.recv(1024)
        if data != b'ok\n\n':
            raise ClientError(message=data.decode())

    def get(self, key):
        try:
            self.sock.sendall(f'get {key}\n'.encode())
            data = self.sock.recv(1024)
            assert len(data) > 0
            if data.startswith(b'error\n'):
                raise AssertionError
            if data.startswith(b'ok\n'):
                return self._parse_response(data)
            else:
                raise AssertionError
        except AssertionError:
            raise ClientError()

    @staticmethod
    def _parse_response(resp_str):
        if resp_str == b'ok\n\n':
            return {}
        result = {}
        resp_str = resp_str.decode().splitlines()
        for idx in range(1, len(resp_str) - 1):
            spam = resp_str[idx].split()
            if spam[0] in result:
                result[spam[0]].append((int(spam[2]), float(spam[1])))
            else:
                result[spam[0]] = [(int(spam[2]), float(spam[1]))]
        return result


class ClientError(Exception):
    def __init__(self, message=''):
        self.input_string = message
