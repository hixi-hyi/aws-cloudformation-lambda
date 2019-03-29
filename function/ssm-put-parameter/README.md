# cfn-lambda-ssm-put-parameter
## Description
The `cfn-lambda-ssm-put-parameter` is `SSM::Parameter` that support `SecureString` and `Region`

## When do you use it
* Put on secret infomation like `!GetAtt AWS::IAM::AccessKey.SecretAccessKey` into SSM::Parameter as SecureString.
* Put on `Arn` that can only be created in a specific region such as ACM into other region.

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
    Policies:
        Deletion:
            - Delete
```
## Parameters

### Name
- [Docs](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-name)
- ***Required:*** Yes
- ***Update requires:*** Replacement

### Type
- [Docs](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-type)
- The `SecureString` parameter type is supported.
- ***Required:*** Yes
- ***Update requires:*** Replacement


### Value (required) [No interruption]
- [Docs](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-value)
- ***Required:*** Yes
- ***Update requires:*** No interruption

### Region (optional) [Replacement]
- [Docs](https://docs.aws.amazon.com/general/latest/gr/rande.html)
- The region outside the default are also supported.
- Default parameter is `AWS::Region`.
- ***Required:*** No
- ***Update requires:*** Replacement

### Policies.Deletion (optional)
- [Docs](../../README.md)
- Support values are `IgnoreError` `Delete` `Retain`.
- Default is `Delete`.
- ***Required:*** No
- ***Update requires:*** No interruption


## ToDO
- Support kms
