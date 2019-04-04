# cfn-lambda-ssm-secret
## Description
The `cfn-value` function define a constant in outside `Parameter`.

## When do you use it
* Define a constant to use repeatdly in AWS::CloudFormation

## Deploy
```
./script/deploy-function.sh value
```

## Usage
```
Resources:
  Domain:
    Type: Custom::Value
    Properties:
      ServiceToken: !ImportValue cfn-lambda-value:LambdaArn
      Value:
        Fn::Join:
          - "."
            - !Ref Environment
            - "example.com"
Outputs:
  OutputDomain:
    Value: !Ref Domain
```
## Parameters
### Value
- Define the value
- ***Required:*** Yes
- ***Update requires:*** Replacement
