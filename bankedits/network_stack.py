from aws_cdk import (
    aws_ec2 as ec2,
    aws_s3_assets as s3,
    aws_iam as iam,
    core,
)

class NetworkStack(core.Stack):

    @property
    def vpc(self):
        return self._vpc

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        VPC_ID = 'bankedits-vpc'
        VPC_CIDR = '10.0.0.0/20'
        MAX_AZS = 2

        self._vpc = ec2.Vpc(self, id=VPC_ID, cidr=VPC_CIDR, max_azs=MAX_AZS)
