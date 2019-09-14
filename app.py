#!/usr/bin/env python3

from aws_cdk import core
from bankedits.app_stack import AppStack

REGION = 'ap-southeast-2'

app = core.App()
AppStack(app, "bankedits", env={'region': REGION})

app.synth()
