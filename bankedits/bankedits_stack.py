from aws_cdk import (
    aws_ec2 as ec2,
    aws_s3_assets as s3,
    aws_iam as iam,
    core,
)

class BankeditsStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        VPC_ID = 'bankedits-vpc'
        VPC_CIDR = '10.0.0.0/20'
        MAX_AZS = 2

        INSTANCE_TYPE = ec2.InstanceType('t2.nano')
        KEYNAME = 'aws-syd'
        ami = ec2.AmazonLinuxImage()

        self._vpc = ec2.Vpc(self, id=VPC_ID, cidr=VPC_CIDR, max_azs=MAX_AZS)

        # IAM Role
        self._role = iam.Role(self, id='role', assumed_by=iam.ServicePrincipal('ec2.amazonaws.com'))
        
        # S3
        files = s3.Asset(self, id='files', path='files')
        files.grant_read(self._role)

        # Security Group
        self._security_group = ec2.SecurityGroup(
            self, id='security_group', vpc=self._vpc, security_group_name='bankedits')
        self._security_group.add_ingress_rule(
            peer=ec2.Peer.ipv4('0.0.0.0/0'), connection=ec2.Port.tcp(22),
            description='Allow SSH traffic')
        
        # Instance
        self._instance = ec2.Instance(self, id='instance', instance_type=INSTANCE_TYPE,
            vpc=self._vpc,
            #key_name=KEYNAME,
            role=self._role, machine_image=ami,
            security_group=self._security_group,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC))

        self._instance.add_user_data(
            'aws s3 cp s3://{}/{} .'.format(files.s3_bucket_name, files.s3_object_key),
            'unzip *.zip -d /tmp',
            'chmod +x /tmp/build.sh; /tmp/build.sh'
        )

        # Tags
        core.Tag.add(self._instance, 'Project', 'bankedits')
