#!/bin/bash
if [ -z "$2" ]; then
  echo "usage: $0 \${bucket} \${file}"
  exit 1
fi
bucket=$1
file=$2

localsize=$(stat --printf "%s" ${file})
remotesize=$(aws s3api head-object --bucket ${bucket} --key ${file} --query "ContentLength" --output "text" 2> /dev/null)

if [ "${localsize}" == "${remotesize}" ]; then
    aws s3api head-object --bucket ${bucket} --key ${file} --query "VersionId" --output "text"
    exit 1
else
    aws s3api put-object --bucket ${bucket} --key ${file} --body ${file} --query 'VersionId' --output 'text'
    exit 0
fi
