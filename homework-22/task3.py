from abc import ABC, abstractmethod


def validate_abstract_methods(cls, abstract_class):
    missing_methods = []

    for method_name in abstract_class.__abstractmethods__:
        if not hasattr(cls, method_name):
            missing_methods.append(method_name)

    return missing_methods

class Stream(ABC):
    @abstractmethod
    def receive(self):
        pass

    @abstractmethod
    def send(self, msg):
        pass

    @abstractmethod
    def close(self):
        pass


class SocketStream(Stream, ABC):
    def receive(self):
        print('Receive')

    def close(self):
        print('Close')


missing_methods = validate_abstract_methods(SocketStream, Stream)

s = SocketStream()
s.send('Hello world')
s.receive()
s.close()
