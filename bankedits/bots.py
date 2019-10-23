from aws_cdk import (
    aws_ec2 as ec2,
    aws_s3_assets as s3,
    aws_iam as iam,
    core,
)

class WikiBot(core.Stack):

    def __init__(self, scope: core.Construct, 
        id: str,
        vpc: ec2.Vpc,
        project_name: str,
        instance_config: dict,
        ssh_config: dict,
        build_files: s3.Asset,
        iam_role: iam.Role = None,
        **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # IAM Role
        if iam_role is None:
            self._role = iam.Role(self, id='role', assumed_by=iam.ServicePrincipal('ec2.amazonaws.com'))
        else:
            self._role = iam_role

        # Security Group
        self._security_group = ec2.SecurityGroup(
            self, id='security_group', vpc=vpc, security_group_name=project_name)
        
        if ssh_config is not None:
            self._security_group.add_ingress_rule(
                peer=ec2.Peer.ipv4(ssh_config['cidr']), connection=ec2.Port.tcp(22),
                description='Allow SSH traffic')

        subnet = ec2.SubnetType.PUBLIC

        # Instance
        self._instance = ec2.Instance(self, id='instance', instance_type=instance_config['instance_type'],
            vpc=vpc, key_name=instance_config['key_name'], role=self._role,
            machine_image=instance_config['ami'], security_group=self._security_group,
            vpc_subnets=ec2.SubnetSelection(subnet_type=subnet))

        # User data
        self._instance.add_user_data(
            'aws s3 cp s3://{}/{} .'.format(build_files.s3_bucket_name, build_files.s3_object_key),
            'unzip *.zip -d /tmp',
            # 'echo \'{ "Test": ["{}"] }\' > /tmp/ranges.json'.format(ssh_config['cidr']),
            'chmod +x /tmp/build.sh; /tmp/build.sh {}'.format(project_name)
        )

        # Tags
        core.Tag.add(self._instance, 'Project', project_name)
