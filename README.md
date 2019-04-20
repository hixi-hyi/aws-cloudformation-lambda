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
### ssm-put-parameter
#### deploy function
```
./script/deploy-function.sh ssm-put-parameter
```
#### test
```
./script/run-test.sh ssm-put-parameter
```
#### deploy demo stack
```
./script/deploy-demo.sh ssm-put-parameter
```
- [ssm-secret](/function/ssm-secret)
- [value](/function/value)
- [strings](/function/strings)
- [cloudformation-stack](/function/cloudformation-stack)
