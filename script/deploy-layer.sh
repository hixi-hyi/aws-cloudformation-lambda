#!/bin/bash
if [ -z "$1" ]; then
  echo "usage: $0 \${function}"
  exit 1
fi
layer=$1
bucket=$(aws cloudformation list-exports --query "Exports[?Name==\`cfn-lambda-s3:BucketName\`].Value" --output "text")

(cd layer/${layer} > /dev/null && zip -q -r ../${layer}.zip ./python)

script/deploy-if-file-updated.sh $bucket layer/${layer}.zip > /dev/null
err=$?
if [ $err -gt 0 ]; then
    echo "${layer}: no changes"
else
    echo "${layer}: updated"
fi
