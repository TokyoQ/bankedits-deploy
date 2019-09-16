from aws_cdk import (
    aws_ec2 as ec2,
    aws_s3_assets as s3,
    aws_iam as iam,
    core,
)

class AppStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, vpc: ec2.Vpc, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        INSTANCE_TYPE = ec2.InstanceType('t2.nano')
        KEYNAME = 'aws-syd'
        SSH_CIDR = '0.0.0.0/0'
        ami = ec2.AmazonLinuxImage()

        # IAM Role
        self._role = iam.Role(self, id='role', assumed_by=iam.ServicePrincipal('ec2.amazonaws.com'))
        
        # S3
        files = s3.Asset(self, id='files', path='files')
        files.grant_read(self._role)

        # Security Group
        self._security_group = ec2.SecurityGroup(
            self, id='security_group', vpc=vpc, security_group_name='bankedits')

        # Public Instance for debugging        
        # self._security_group.add_ingress_rule(
        #     peer=ec2.Peer.ipv4(SSH_CIDR), connection=ec2.Port.tcp(22),
        #     description='Allow SSH traffic')
        self._instance = ec2.Instance(self, id='instance', instance_type=INSTANCE_TYPE,
            vpc=vpc, key_name=KEYNAME, role=self._role, machine_image=ami,
            security_group=self._security_group,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC))

        # Private instance - no ssh
        # self._instance = ec2.Instance(self, id='instance', instance_type=INSTANCE_TYPE,
        #     vpc=self._vpc, key_name=KEYNAME, role=self._role, machine_image=ami,
        #     security_group=self._security_group,
        #     vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE))

        self._instance.add_user_data(
            'aws s3 cp s3://{}/{} .'.format(files.s3_bucket_name, files.s3_object_key),
            'unzip *.zip -d /tmp',
            'chmod +x /tmp/build.sh; /tmp/build.sh'
        )

        # Tags
        core.Tag.add(self._instance, 'Project', 'bankedits')
