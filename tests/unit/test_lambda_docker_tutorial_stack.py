import aws_cdk as core
import aws_cdk.assertions as assertions

from lambda_docker_tutorial.lambda_docker_tutorial_stack import LambdaDockerTutorialStack

# example tests. To run these tests, uncomment this file along with the example
# resource in lambda_docker_tutorial/lambda_docker_tutorial_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = LambdaDockerTutorialStack(app, "lambda-docker-tutorial")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
