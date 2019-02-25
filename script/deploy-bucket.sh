#!/bin/bash
aws cloudformation deploy --stack-name cfn-lambda-s3 --template-file setup/bucket.yaml
