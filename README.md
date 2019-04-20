# aws-cloudformation-lambda

The repository provides cloudformation-lambda (cloudformation custom resource).
See [here](/function) for a list of functions.

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
- [ssm-secret](https://github.com/hixi-hyi/aws-cloudformation-lambda-ssm-secret/)
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
