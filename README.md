## Lambda duplicate invocation handler

Async event sources that trigger a Lambda function guarantee it's execution **_at least once_**. Considering that all Serverless application's need to leverage an Async service (eg. SNS, CloudWatch events, etc) in some form, this is a big deal.

This repo demonstrates how to handle such duplicate invocations.