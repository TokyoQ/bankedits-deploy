# bankedits-deploy

A cdk app which deploys [@bankedits](https://twitter.com/bankedits) onto AWS.

## Environment

The application will create a new VPC with 2 public subnets only to avoid the need to run a NAT instance. There is a `dev` and `prod` stack for each bot. The dev version will add a security group to allow ssh access for debugging purposes.

## Build

1. You will need to create a Twitter developer account and create an app to generate your own access tokens to use the API.
2. In the [files](files) folder, create a file called `.bankedits.secret` with the below format and specify your credentials.
```
    consumer_key=xxx 
    consumer_secret=xxx
    access_token=xxx
    access_token_secret=xxx
```
3. Create a virtualenv (recommended)
    `python3 -m venv .env`
    `source .env/bin/activate`
4. Install the cdk `npm install -g aws-cdk`
5. `pip install -r requirements.txt`
6. Set up your aws credentials file (~/.aws/credentials)
7. `cdk bootstrap`
8. `cdk deploy core`
8. `cdk deploy network`
8. `cdk deploy bankedits-dev`

## Other Bots

The deployment now supports multiple bots such as [@techedits](https://twitter.com/tech_edits)

These contain their own stacks which you can run independently.
