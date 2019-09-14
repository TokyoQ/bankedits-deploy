#!/usr/bin/env python3

from aws_cdk import core
from bankedits.bankedits_stack import BankeditsStack

REGION = 'ap-southeast-2'

app = core.App()
BankeditsStack(app, "bankedits", env={'region': REGION})

app.synth()
