# cfn-lambda-ssm-put-parameter
## Description

## Deploy
```
aws cloudformation deploy --template-file ssm-put-parameter.yaml --stack-name cfn-lambda-ssm-put-parameter --capabilities CAPABILITY_NAMED_IAM
```
## Usage
```
AccessKeySecret:
  Type: Custom::SsmParameter
  Properties:
    ServiceToken: !ImportValue cfn-lambda-ssm-put-parameter:LambdaArn
    Name: /user/hixi/access-key-secret
    Type: SecureString
    Value: !GetAtt HixiAccessKey.SecretAccessKey
    Region: !Ref AWS::Region
    DeletionPolicy: Delete
```
## Parameters

### Name (required)
- [Docs](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-name)

### Type (required)
- [Docs](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-type)
- The `SecureString` parameter type supported.

### Value (required)
- [Docs](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-value)

### Region (optional)
- [Docs](https://docs.aws.amazon.com/general/latest/gr/rande.html)
- Default parameter is `AWS::Region`.

### DeletionPolicy (optional)
- [Docs](https://github.com/hixi-hyi/aws-cloudformation-lambda/README.md)
- Support values are `IgnoreError` `Delete` `Retain`.
- Default is `Retain`.


## ToDO
- Support kms

