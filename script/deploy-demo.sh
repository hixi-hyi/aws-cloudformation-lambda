#!/bin/bash
if [ -z "$1" ]; then
  echo "usage: $0 \${function}"
  exit 1
fi
function=$1
if [ "$function" == "cloudformation-stack" ]; then
    bucket=$(aws cloudformation list-exports --query "Exports[?Name==\`cfn-lambda-s3:BucketName\`].Value" --output "text")
    aws s3api put-object --bucket ${bucket} --key demo/cloudformation-stack/resource.yaml --body function/cloudformation-stack/tests/resource.yaml > /dev/null
fi
date=$(date)
aws cloudformation deploy --stack-name cfn-lambda-${function}-demo --template-file demo/${function}/demo.yaml --parameter-overrides Date="$date"
