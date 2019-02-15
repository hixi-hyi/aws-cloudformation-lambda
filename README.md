# aws-cloudformation-lambda

## ssm-put-parameter.yaml

### deploy
```
aws cloudformation deploy --template-file ssm-put-parameter.yaml --stack-name cfn-lambda-ssm-put-parameter --capabilities CAPABILITY_NAMED_IAM
```

### usage
```
AccessKeySecret:
  Type: Custom::CfnLambda
  Properties:
    ServiceToken: !ImportValue cfn-lambda-ssm-put-parameter:LambdaArn
    Region: !Ref AWS::Region
    Name: /user/hixi/access-key-secret
    Value: !GetAtt HixiAccessKey.SecretAccessKey
    Type: SecureString
    DeletionPolicy: Delete
```
