# aws-cloudformation-lambda

## Setup
1. [setup the s3 bucket](/setup)
```
./script/deploy-bucket.sh
```
2. [deploy the base layer](/layer/cfnprovider)
```
./script/deploy-layer.sh cfnprovider
```

## Functions
- [ssm-put-parameter](/function/ssm-put-parameter)
```
./script/deploy-function.sh ssm-put-parameter
```
