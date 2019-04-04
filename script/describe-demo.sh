#!/bin/bash
if [ -z "$1" ]; then
  echo "usage: $0 \${function}"
  exit 1
fi
function=$1
aws cloudformation describe-stacks --stack-name cfn-lambda-${function}-demo
