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

    client.zip()
    print('run oneway function zip(), done')
    time.sleep(sleepSeconds)

    client.ping()
    print('ping()')
    time.sleep(sleepSeconds)

    client.zip()
    print('run oneway function zip(), done')
    time.sleep(sleepSeconds)

    sum_ = client.add(1, 1)
    print('1+1=%d' % sum_)
    time.sleep(sleepSeconds)

    work = Work()

    work.op = Operation.DIVIDE
    work.num1 = 1
    work.num2 = 0

    try:
        quotient = client.calculate(1, work)
        print('Whoa? You know how to divide by zero?')
        print('FYI the answer is %d' % quotient)
    except InvalidOperation as e:
        print('InvalidOperation: %r' % e)
    time.sleep(sleepSeconds)

    work.op = Operation.SUBTRACT
    work.num1 = 15
    work.num2 = 10

    diff = client.calculate(1, work)
    print('15-10=%d' % diff)
    time.sleep(sleepSeconds)

    log = client.getStruct(1)
    print('Check log: %s' % log.value)
    time.sleep(sleepSeconds)
    

    # Close!
    transport.close()

main()

