#!/bin/bash
if [ -z "$1" ]; then
  echo "usage: $0 \${function}"
  exit 1
fi
function=$1
date=$(date)
aws cloudformation deploy --stack-name cfn-lambda-${function}-demo --template-file demo/${function}/demo.yaml --parameter-overrides Date="$date"
