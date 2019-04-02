
def get_context():
  return {}

def get_create_event(properties):
  return {
    "RequestType": "Create",
    "ResponseURL": "http://pre-signed-S3-url-for-response",
    "StackId": "arn:aws:cloudformation:ap-northeast-1:123456789012:stack/MyStack/guid",
    "RequestId": "1234567890",
    "ResourceType": "Custom::TestResource",
    "LogicalResourceId": "MyTestResource",
    "ResourceProperties": properties,
  }
