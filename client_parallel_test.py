#! /usr/bin/env python3

import sys
import glob
import time
sys.path.append('gen-py')
# sys.path.insert(0, glob.glob('../../lib/py/build/lib*')[0])

from tutorial import Calculator
from tutorial.ttypes import InvalidOperation, Operation, Work

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


def main():
    sleepSeconds = 0   # TODO

    # Make socket
    transport = TSocket.TSocket('localhost', 9090)

    # Buffering is critical. Raw sockets are very slow
    transport = TTransport.TBufferedTransport(transport)

    # Wrap in a protocol
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    # Create a client to use the protocol encoder
    client = Calculator.Client(protocol)

    # Connect!
    transport.open()


    print('start ping')
    client.ping()
    print('end ping')
    time.sleep(1)

    print('start ping')
    client.ping()
    print('end ping')
    time.sleep(1)

    print('start ping')
    client.ping()
    print('end ping')
    time.sleep(1)

    print('start add')
    sum_ = client.add(1, 1)
    print('1+1=%d' % sum_)
    time.sleep(sleepSeconds)

    print('start add')
    sum_ = client.add(1, 1)
    print('1+1=%d' % sum_)
    time.sleep(sleepSeconds)





    # Close!
    transport.close()

main()

