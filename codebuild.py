from troposphere import Ref, Template
import troposphere.codebuild as codebuild
from troposphere.codebuild import Artifacts, Environment, Source, Project, WebhookFilter, ProjectTriggers

template = Template()
template.add_version('2010-09-09')

artifacts = Artifacts(Type='NO_ARTIFACTS')

environment = Environment(
    ComputeType='BUILD_GENERAL1_SMALL',
    Image='470820891875.dkr.ecr.eu-west-1.amazonaws.com/bbc-centos8-ci',
    ImagePullCredentialsType='SERVICE_ROLE',
    Type='LINUX_CONTAINER'
)

source = Source(
    Location='https://github.com/icottambbc/hello-world-lambda',
    Type='GITHUB'
)

projectTriggers = ProjectTriggers(
  Webhook=True
)

project = Project(
    "CloudFormedHWL12321",
    Artifacts=artifacts,
    Environment=environment,
    Name='CloudFormedHWL12321',
    ServiceRole='arn:aws:iam::555778779797:role/service-role/ALLOW_PUBLISH_2',
    Source=source,
    Triggers=projectTriggers
)


template.add_resource(project)
print(template.to_json())
