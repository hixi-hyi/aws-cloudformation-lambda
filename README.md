# aws-cloudformation-lambda

The repository provides cloudformation-lambda (cloudformation custom resource).
See [here](/function) for a list of functions.

## Deploy
### Setup
1. [setup the s3 bucket](/setup)
```
./script/deploy-bucket.sh
```
2. [deploy the base layer](/layer/cfnprovider)
```
./script/deploy-layer.sh cfnprovider
```

### Deploy functions
```
./script/deploy-function.sh ${function}
```

## Functions
- [ssm-secret](https://github.com/hixi-hyi/aws-cloudformation-lambda-ssm-secret)
- [ssm-put-parameter](https://github.com/hixi-hyi/aws-cloudformation-lambda-ssm-put-parameter)
- [value](https://github.com/hixi-hyi/aws-cloudformation-lambda-value)
- [strings](https://github.com/hixi-hyi/aws-cloudformation-lambda-strings)
- [cloudformation-stack](https://github.com/hixi-hyi/aws-cloudformation-lambda-cloudformation-stack)


## Contributing
### Test functions
```
./script/run-test.sh ${function}
```
### Deploy demo stack
```
./script/deploy-demo.sh ${function}
```
