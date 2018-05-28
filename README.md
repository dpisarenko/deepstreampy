# deepstreampy

A Python client for deepstream.io

[![Build Status](https://travis-ci.org/YavorPaunov/deepstreampy.svg)](https://travis-ci.org/YavorPaunov/deepstreampy)
[![Coverage Status](https://coveralls.io/repos/github/YavorPaunov/deepstreampy/badge.svg)](https://coveralls.io/github/YavorPaunov/deepstreampy)

# Intellectual Property

This is an attempt to extend the Python client library written by [Yavor Paunov](https://github.com/YavorPaunov/deepstreampy). He is the original author of this software.

# Contributor's Guide

## Setting up the infrastructure

* Install Python 3.6 on your machine (or 3.5, 3.6, 3.4, 3.3, or 2.7, see [.travis.yml](https://github.com/dpisarenko/deepstreampy/blob/dev/.travis.yml)) 
* Install [pyee](https://pypi.org/project/pyee/) (`pip install pyee`) 
* Install [tornado](https://pypi.org/project/tornado/) (`pip install tornado`) 
* Install [nose](https://nose.readthedocs.io/en/latest/) (`pip install nose`) 

## How to build the project

1. Run `python setup.py build`.
2. The results will be in the `build/lib/deepstreampy/` directory.

[Source](https://pythonhosted.org/an_example_pypi_project/setuptools.html)

## How to create a binary distribution

1. Run `python setup.py bdist`.
2. The `dist` directory will contain the generated files. 

[Source](https://pythonhosted.org/an_example_pypi_project/setuptools.html)

## How to run tests

1. Go (`cd`) into the project directory.
2. Run `nosetests` in the command line.

## How to install DeepStream under Windows 

As of this writing (18.04.2018) there is no working Windows binary available (see [issue #893](https://github.com/deepstreamIO/deepstream.io/issues/893)). There are at least two work-arounds:

1. Build the binary from the sources.
2. Install Deepstream in the Windows Ubuntu subsystem (as described [here](https://deepstreamhub.com/open-source/install/ubuntu/)).
 
## How to find out how the DeepStream server works

For this we'll need to use one of the existing DeepStream clients. I will use the JavaScript client.

To set it up, following things need to be done:

### Step 1: Set up authentication

I assume that DeepStream server is already installed at this point. Now we need to set up a [simple authentication mechanism](https://deepstreamhub.com/open-source/core/auth-file/).

Change the authentication section of the `/etc/deepstream/config.yml` file so that it looks like this:

```
auth:
  type: file
  options:
    path: ./users.yml # Path to the user file. Can be json, js or yml
    hash: 'md5' # the name of a HMAC digest algorithm
    iterations: 100 # the number of times the algorithm should be applied
    keyLength: 32 # the length of the resulting key
```

Deepstream comes with a file `/etc/deepstream/users.yml` that contains one user `userA`. 

### Step 2: Install JavaScript client library
 
Install the client library using `npm install deepstream.io-client-js --save` [source](https://deepstreamhub.com/docs/).


 
## How to manually test the library

1. Install [DeepStream](https://deepstreamhub.com/open-source/#install) on your machine. If you are using Windows and [issue #893](https://github.com/deepstreamIO/deepstream.io/issues/893) is not resolved, read section "How to install DeepStream under Windows". 
2. Build and install the deepstreampy library (`python setup.py install`).   
3. Configure a test user.

# Questions asked by Python newbies

## Q: What does `setup.py` do?

Looks like the equivalent of [pom.xml](https://en.wikipedia.org/wiki/Apache_Maven#Project_Object_Model) file in the Java world or Makefile in C, according to [StackOverflow](https://stackoverflow.com/questions/1471994/what-is-setup-py). 

# Progress

The [DeepStream.io spec](https://github.com/deepstreamIO/deepstream.io-client-specs) contains the features shown below. The DeepStream Python client is completed, if all these features are implemented (with exceptions, see Wolfram Hempel's [comment](https://github.com/deepstreamIO/deepstream.io/issues/72)). 

| Nr. | Feature | Is it implemented? | Notes |
| --- | ------- | ------------------ | ----- |
|1|[Parsing messages](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/message-parsing.feature)|Unknown||
|2|[Connecting a client](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/connecting/connecting.feature)|Unknown||
|3|[Heartbeats](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/connecting/connection-heartbeat.feature)|Unknown||
|4|[Redirecting the client to another deepstream gets rejected](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/connecting/connection-invalid-redirect.feature)|Unknown||
|5|[Redirecting a client to another deepstream](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/connecting/connection-redirect.feature)|Unknown||
|6|[Logging In](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/connecting/logging-in.feature)|Yes|`examples-js/feature-06-logging-in.js`, `examples/feature-06-logging-in.py`|
|7|[Events Misc](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/events/event-misc.feature)|Unknown||
|8|[Events Connectivity](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/events/events-connection.feature)|Unknown||
|9|[Event Listen Timeouts](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/events/events-listen-timeouts.feature)|Unknown||
|10|[Event Listen](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/events/events-listen.feature)|Unknown||
|11|[Events Timeouts](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/events/events-timeouts.feature)|Unknown||
|12|[Events](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/events/events.feature)|Unknown||
|13|[Presence Connectivity](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/presence/presence-connection.feature)|Unknown||
|14|[Presence](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/presence/presence-querying.feature)|Unknown||
|15|[Presence (global listener)](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/presence/presence-subscriptions-all.feature)|Unknown||
|16|[Presence (individual listeners)](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/presence/presence-subscriptions-individual.feature)|Unknown||
|17|[Presence Timeouts](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/presence/presence-timeouts.feature)|Unknown||
|18|[Record Conflicts](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/record/record-conflicts.feature)|Unknown||
|19|[Record Connectivity](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/record/record-connection.feature)|Unknown||
|20|[Record Has](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/record/record-has.feature)|Unknown||
|21|[Record Listen Timeouts](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/record/record-listen-timeouts.feature)|Unknown||
|22|[Record Listen](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/record/record-listen.feature)|Unknown||
|23|[Record Misc](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/record/record-misc.feature)|Unknown||
|24|[Record Snapshot](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/record/record-snapshot.feature)|Unknown||
|25|[Record Subscription](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/record/record-subscription.feature)|Unknown||
|26|[Record Timeouts](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/record/record-timeouts.feature)|Unknown||
|27|[Record write acknowledgement](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/record/record-writeAcknowledgement.feature)|Unknown||
|28|[Record](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/record/record.feature)|Unknown||
|29|[RPC Connectivity](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/rpc/rpc-connection.feature)|Unknown||
|30|[Providing RPC](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/rpc/rpc-provider.feature)|Unknown||
|31|[Requesting an RPC](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/rpc/rpc-requestor.feature)|Unknown||
|32|[RPC Timeouts](https://github.com/deepstreamIO/deepstream.io-client-specs/blob/master/rpc/rpc-timeouts.feature)|Unknown||

