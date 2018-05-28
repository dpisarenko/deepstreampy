"""
An example showing how to check who is logged into the deepstream.io server and
listen for changes.
"""
from __future__ import absolute_import, division, print_function, with_statement
from __future__ import unicode_literals

from deepstreampy import connect
from deepstreampy import presence

from tornado import gen
from tornado import ioloop

import signal

@gen.coroutine
def run():
    client = yield connect("ws://localhost:6020/deepstream")
    result = yield client.login({"username": "userA", "password": "password"})
    print("result: " + str(result['success']))

if __name__ == "__main__":
    run()
    signal.signal(signal.SIGINT, lambda _, __: ioloop.IOLoop.current().stop())
    ioloop.IOLoop.current().start()
