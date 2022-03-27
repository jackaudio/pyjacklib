#!/bin/bash
#
# run unit tests with proper pytest invocation
#

if [ $# = 0 ]; then
    exec ${PYTHON:-python} -m pytest -v --strict-markers tests/
fi
    exec ${PYTHON:-python} -m pytest -v --strict-markers "$@"
fi
