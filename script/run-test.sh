#!/bin/bash
if [ -z "$1" ]; then
  echo "usage: $0 \${function}"
  exit 1
fi
function=$1
(cd function/${function} && PYTHONPATH="../../test:../../layer/cfnprovider/python:$PYTHONPATH" python -m unittest discover tests)
