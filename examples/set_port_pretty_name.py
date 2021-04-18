#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

import jacklib
from jacklib.helpers import get_jack_status_error_string


if len(sys.argv) == 3:
    portname = sys.argv[1]
    pretty_name = sys.argv[2]
else:
    sys.exit("Usage: %s <port name> <pretty-name>" % sys.argv[0])

status = jacklib.jack_status_t()
client = jacklib.client_open("set-port-pretty-name", jacklib.JackNoStartServer, status)
err = get_jack_status_error_string(status)

if status.value:
    if status.value & jacklib.JackNameNotUnique:
        print("Non-fatal JACK status: %s" % err, file=sys.stderr)
    elif status.value & jacklib.JackServerStarted:
        # Should not happen, since we use the JackNoStartServer option
        print("Unexpected JACK status: %s" % err, file=sys.stderr)
    else:
        sys.exit("Error connecting to JACK server: %s" % err)

res = jacklib.set_port_pretty_name(client, portname, pretty_name)
if res != -1:
    print("Pretty name for port '%s' is now '%s'." % (portname, pretty_name))


jacklib.client_close(client)
