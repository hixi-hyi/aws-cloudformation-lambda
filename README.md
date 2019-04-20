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

## Deploy functions
```
./script/deploy-function.sh ${function}
```

## Functions
- [ssm-secret](/function/ssm-secret)
- [ssm-put-parameter](/function/ssm-put-parameter)
- [value](/function/value)
- [strings](/function/strings)
- [cloudformation-stack](/function/cloudformation-stack)


## Contributing
### Test functions
```
./script/run-test.sh ${function}
```
### Deploy demo stack
```
./script/deploy-demo.sh ${function}
```
