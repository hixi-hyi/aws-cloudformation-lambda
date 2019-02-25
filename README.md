# aws-cloudformation-lambda

## Setup
1. setup the s3 bucket
[setup](/setup)
```
./script/deploy-bucket.sh
```
2. deploy the base layer
[custom-resource-provider](/layer/cfnprovider)
```
./script/deploy-layer.sh cfnprovider
```

## Functions
- [ssm-put-parameter](/function/ssm-put-parameter)
```
./script/deploy-function.sh ssm-put-parameter
```

## Common parameters
### CreationPolicy
- UseIfExists
- Overwrite
### UpdatePolicy
- Retain
- Update
### DeletionPolicy
- IgnoreError
- Retain
- Delete

## ToDo
- Supports the `RoleArn` property on resource definition. The current role which defined by function may have strong permissions.
