#!/usr/bin/env python3

from aws_cdk import core
from bankedits.network_stack import NetworkStack
from bankedits.app_stack import AppStack

REGION = 'ap-southeast-2'

app = core.App()
network = NetworkStack(app, "core", env={'region': REGION})
vpc = network.vpc

AppStack(app, "bankedits-public", vpc, public=True, env={'region': REGION})
AppStack(app, "bankedits-private", vpc, env={'region': REGION})

app.synth()
