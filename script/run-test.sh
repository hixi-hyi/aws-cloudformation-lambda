#!/bin/bash
if [ -z "$1" ]; then
  echo "usage: $0 \${function}"
  exit 1
fi
function=$1
(cd function/${function} && PYTHONPATH="../../test:../../layer/cfnprovider/python:$PYTHONPATH" AWS_ACCESS_KEY_ID=fake AWS_SECRET_ACCESS_KEY=fake AWS_DEFAULT_REGION=ap-northeast-1 python -m unittest discover tests -v)
