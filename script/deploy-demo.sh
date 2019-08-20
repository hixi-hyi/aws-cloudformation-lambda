#!/bin/bash
if [ -z "$1" ]; then
  echo "usage: $0 \${function}"
  exit 1
fi
function=$1; shift
demo=${1:demo}; shift
if [ "$function" == "cloudformation-stack" ]; then
    bucket=$(aws cloudformation list-exports --query "Exports[?Name==\`cfn-lambda-s3:BucketName\`].Value" --output "text")
    demostack=function/cloudformation-stack/demo/resource.yaml
    aws s3api put-object --bucket ${bucket} --key ${demostack} --body ${demostack} > /dev/null
fi
date=$(date)
aws cloudformation deploy --stack-name cfn-lambda-${function}-demo --template-file function/${function}/demo/${demo}.yaml --parameter-overrides Date="$date" $*
