from aws_cdk import (
    core,
    aws_ec2 as ec2
)
from bankedits.core import Network, Core
from bankedits.bots import WikiBot

# Settings
REGION = 'ap-southeast-2'
VPC_CIDR = '10.20.0.0/24'
INSTANCE_TYPE = 't2.nano'
SSH_KEY_NAME = 'ac-syd-dell'
SSH_CIDR = '49.255.12.162/32'

instance_config = {
    'instance_type': ec2.InstanceType(INSTANCE_TYPE),
    'ami': ec2.AmazonLinuxImage(),
    'key_name': SSH_KEY_NAME
}
ssh_config = {
    'cidr': SSH_CIDR
}

# MAIN
app = core.App()
network = Network(app, "core-network", VPC_CIDR, env={'region': REGION})
core = Core(app, "core-common", env={'region': REGION})

WikiBot(app, "bankedits-dev", network.vpc, 'bankedits', instance_config, ssh_config,
    core.files, core.role, env={'region': REGION})
WikiBot(app, "bankedits-prod", network.vpc, 'bankedits', instance_config, None,
    core.files, core.role, env={'region': REGION})
WikiBot(app, "techedits-dev", network.vpc, 'techedits', instance_config, ssh_config,
    core.files, core.role, env={'region': REGION})
WikiBot(app, "techedits-prod", network.vpc, 'techedits', instance_config, None,
    core.files, core.role, env={'region': REGION})

app.synth()
