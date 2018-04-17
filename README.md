# deepstreampy
A Python client for deepstream.io

[![Build Status](https://travis-ci.org/YavorPaunov/deepstreampy.svg)](https://travis-ci.org/YavorPaunov/deepstreampy)
[![Coverage Status](https://coveralls.io/repos/github/YavorPaunov/deepstreampy/badge.svg)](https://coveralls.io/github/YavorPaunov/deepstreampy)

# Contributor's Guide

## Setting up the infrastructure

* Install Python 3.6 on your machine (or 3.5, 3.6, 3.4, 3.3, or 2.7, see [.travis.yml](https://github.com/dpisarenko/deepstreampy/blob/dev/.travis.yml) 

## How to build the project

`python setup.py build`

[Source](https://pythonhosted.org/an_example_pypi_project/setuptools.html)

# Questions asked by Python newbies

## Q: What does `setup.py` do?

Looks like the equivalent of [pom.xml](https://en.wikipedia.org/wiki/Apache_Maven#Project_Object_Model) file in the Java world or Makefile in C, according to [StackOverflow](https://stackoverflow.com/questions/1471994/what-is-setup-py). 

# Progress

The [DeepStream.io spec](https://github.com/deepstreamIO/deepstream.io-client-specs) contains the features shown below. The DeepStream Python client is completed, if all these features are implemented (with exceptions, see Wolfram Hempel's [comment](https://github.com/deepstreamIO/deepstream.io/issues/72)). 

| Nr. | Feature | Is it implemented? | Notes |
| --- | ------- | ------------------ | ----- |
|1|[https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/message-parsing.feature](1. [Parsing messages](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/message-parsing.feature))|Unknown||
|2|[https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/connecting/connecting.feature](1. [Connecting a client](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/connecting/connecting.feature))|Unknown||
|3|[https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/connecting/connection-heartbeat.feature](1. [Heartbeats](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/connecting/connection-heartbeat.feature))|Unknown||
|4|[https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/connecting/connection-invalid-redirect.feature](1. [Redirecting the client to another deepstream gets rejected](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/connecting/connection-invalid-redirect.feature))|Unknown||
|5|[https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/connecting/connection-redirect.feature](1. [Redirecting a client to another deepstream](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/connecting/connection-redirect.feature))|Unknown||
|6|[https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/connecting/logging-in.feature](1. [Logging In](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/connecting/logging-in.feature))|Unknown||
|7|[https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/events/event-misc.feature](1. [Events Misc](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/events/event-misc.feature))|Unknown||
|8|[https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/events/events-connection.feature](1. [Events Connectivity](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/events/events-connection.feature))|Unknown||
|9|[https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/events/events-listen-timeouts.feature](1. [Event Listen Timeouts](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/events/events-listen-timeouts.feature))|Unknown||
|10|[https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/events/events-listen.feature](1. [Event Listen](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/events/events-listen.feature))|Unknown||
|11|[https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/events/events-timeouts.feature](1. [Events Timeouts](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/events/events-timeouts.feature))|Unknown||
|12|[https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/events/events.feature](1. [Events](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/events/events.feature))|Unknown||
|13|[https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/presence/presence-connection.feature](1. [Presence Connectivity](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/presence/presence-connection.feature))|Unknown||
|14|[https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/presence/presence-querying.feature](1. [Presence](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/presence/presence-querying.feature))|Unknown||
|15|[https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/presence/presence-subscriptions-all.feature](1. [Presence (global listener)](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/presence/presence-subscriptions-all.feature))|Unknown||
|16|[https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/presence/presence-subscriptions-individual.feature](1. [Presence (individual listeners)](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/presence/presence-subscriptions-individual.feature))|Unknown||
|17|[https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/presence/presence-timeouts.feature](1. [Presence Timeouts](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/presence/presence-timeouts.feature))|Unknown||
|18|[https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/record/record-conflicts.feature](1. [Record Conflicts](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/record/record-conflicts.feature))|Unknown||
|19|[https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/record/record-connection.feature](1. [Record Connectivity](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/record/record-connection.feature))|Unknown||
|20|[https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/record/record-has.feature](1. [Record Has](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/record/record-has.feature))|Unknown||
|21|[https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/record/record-listen-timeouts.feature](1. [Record Listen Timeouts](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/record/record-listen-timeouts.feature))|Unknown||
|22|[https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/record/record-listen.feature](1. [Record Listen](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/record/record-listen.feature))|Unknown||
|23|[https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/record/record-misc.feature](1. [Record Misc](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/record/record-misc.feature))|Unknown||
|24|[https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/record/record-snapshot.feature](1. [Record Snapshot](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/record/record-snapshot.feature))|Unknown||
|25|[https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/record/record-subscription.feature](1. [Record Subscription](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/record/record-subscription.feature))|Unknown||
|26|[https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/record/record-timeouts.feature](1. [Record Timeouts](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/record/record-timeouts.feature))|Unknown||
|27|[https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/record/record-writeAcknowledgement.feature](1. [Record write acknowledgement](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/record/record-writeAcknowledgement.feature))|Unknown||
|28|[https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/record/record.feature](1. [Record](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/record/record.feature))|Unknown||
|29|[https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/rpc/rpc-connection.feature](1. [RPC Connectivity](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/rpc/rpc-connection.feature))|Unknown||
|30|[https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/rpc/rpc-provider.feature](1. [Providing RPC](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/rpc/rpc-provider.feature))|Unknown||
|31|[https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/rpc/rpc-requestor.feature](1. [Requesting an RPC](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/rpc/rpc-requestor.feature))|Unknown||
|32|[https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/rpc/rpc-timeouts.feature](1. [RPC Timeouts](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/rpc/rpc-timeouts.feature))|Unknown||

