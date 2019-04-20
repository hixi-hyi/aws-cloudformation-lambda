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
- [ssm-secret](/function/ssm-secret)
- [value](/function/value)
- [strings](/function/value)
