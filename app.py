#!/usr/bin/env python3

from aws_cdk import core
from bankedits.network_stack import NetworkStack
from bankedits.app_stack import AppStack

REGION = 'ap-southeast-2'

app = core.App()
network = NetworkStack(app, "core", env={'region': REGION})
vpc = network.vpc

appstack = AppStack(app, "bankedits", vpc, env={'region': REGION})

app.synth()
