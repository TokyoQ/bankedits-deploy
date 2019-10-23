from aws_cdk import (
    aws_ec2 as ec2,
    aws_s3_assets as s3,
    aws_iam as iam,
    core,
)

class Network(core.Stack):

    @property
    def vpc(self):
        return self._vpc

    # Simple version - only public subnets
    def __init__(self, scope: core.Construct, id: str, vpc_cidr: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        VPC_ID = 'bankedits-vpc'
        MAX_AZS = 2

        subnet_configuration = [
            {'name': 'bankedits-public', 'cidr_mask': vpc_cidr, 'subnetType': ec2.SubnetType.PUBLIC}
        ]

        self._vpc = ec2.Vpc(self, id=VPC_ID, cidr=vpc_cidr, max_azs=MAX_AZS, nat_gateways=0,
            subnet_configuration=subnet_configuration)


class Core(core.Stack):

    @property
    def role(self):
        return self._role

    @property
    def files(self):
        return self._files

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self._role = iam.Role(self, id='role', assumed_by=iam.ServicePrincipal('ec2.amazonaws.com'))

        self._files = s3.Asset(self, id='files', path='files')
        self._files.grant_read(self._role)
