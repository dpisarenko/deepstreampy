"""
An example of login functionality.
"""
from __future__ import absolute_import, division, print_function, with_statement
from __future__ import unicode_literals

from deepstreampy import connect
from deepstreampy import rpc

from tornado import gen
from tornado import ioloop

import signal

@gen.coroutine
def run():
    print("Connecting")
    provider = yield connect("ws://localhost:6020")
    print("After connection, provider:" + provider)

if __name__ == "__main__":
    print("Before calling run")
    run()
    signal.signal(signal.SIGINT, lambda _, __: ioloop.IOLoop.current().stop())
    ioloop.IOLoop.current().start()
