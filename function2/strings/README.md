# cfn-lambda-strings
## Description
The `cfn-lambda-strings` function privide to some strings function.

## When do you use it
* Build a string value based on the `Parameter`
* Name the cloudformation resoueces.
 * e.g. `MetricName` in AWS::WAF::Rule allowed only alphanumeric character, so you can choose Camelize. `Name` in AWS::WAF::Rule allowed user friendly name, so you can choose Titlize.

## Deploy
```
./script/deploy-function.sh strings
```

## Examples
```
Resources:
  Id:
    Type: Custom::Value
    Properties:
      ServiceToken: !ImportValue cfn-lambda-strings:LambdaArn
      Values:
        - !Ref Environment
        - !Ref AWS::StackName
Outputs:
  Output:
    Value: !GetAtt Target.Camelize
```
## Properties
### Values
- List of string that you want to convert.
- ***Type:*** List of String
- ***Required:*** Yes
- ***Update requires:*** Replacement

## Return Values
### !Ref
### !GetAtt Upper
- Convert value(s) to upper case.
- ***For examples:*** HIXIDEV if the properties are ['hIxi', 'dEv']
### !GetAtt Lower
- Convert value(s) to lower case.
- ***For examples:*** hixidev if the properties are ['hIxi', 'dEv']
### !GetAtt Camelize
- Convert values to upper camel case.
- ***For examples:*** HixiDev if the properties are ['hIxi', 'dEv']
### !GetAtt CamelizeLower
- Convert values to lower camel case.
- ***For examples:*** hixiDev if the properties are ['hIxi', 'dEv']
### !GetAtt Dasherize
- Convert values to concatenate with `-`.
- ***For examples:*** hIxi-dEv if the properties are ['hIxi', 'dEv']
### !GetAtt DasherizeLower
- Convert values to lower case and concatenate with `-`.
- ***For examples:*** hixi-dev if the properties are ['hIxi', 'dEv']
### !GetAtt DasherizeUpper
- Convert values to upper case and concatenate with `-`.
- ***For examples:*** HIXI-DEV if the properties are ['hIxi', 'dEv']
### !GetAtt Snakelize
- Convert values to concatenate with `_`.
- ***For examples:*** hIxi\_dEv if the properties are ['hIxi', 'dEv']
### !GetAtt SnakelizeLower
- Convert values to lower case and concatenate with `-`.
- ***For examples:*** hixi\_dev if the properties are ['hIxi', 'dEv']
### !GetAtt SnakelizeUpper
- Convert values to upper case and concatenate with `-`.
- ***For examples:*** HIXI\_DEV if the properties are ['hIxi', 'dEv']
### !GetAtt Dotlize
- Convert values to concatenate with `.`.
- ***For examples:*** hIxi.dEv if the properties are ['hIxi', 'dEv']
### !GetAtt DotlizeLower
- Convert values to lower case and concatenate with `.`.
- ***For examples:*** hixi.dev if the properties are ['hIxi', 'dEv']
### !GetAtt DotlizeUpper
- Convert values to upper case and concatenate with `.`.
- ***For examples:*** HIXI.DEV if the properties are ['hIxi', 'dEv']
### !GetAtt Titlize
- Convert values to title case.
- ***For examples:*** Hixi Dev if the properties are ['hIxi', 'dEv']
