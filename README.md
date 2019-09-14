# bankedits-deploy

A cdk app which deploys [@bankedits](https://twitter.com/bankedits) onto AWS.

## Build

1. You will need to create a Twitter developer account and create an app to generate your own access tokens to use the API.
2. In the [files](files) folder, create a file called `.secret` with the below format and specify your credentials.
    consumer_key=xxx
    consumer_secret=xxx
    access_token=xxx
    access_token_secret=xxx
3. Install the cdk `npm install -g aws-cdk`
4. `pip install -r requirements.txt`
5. Set up your aws credentials file (~/.aws/credentials)
5. `cdk deploy bankedits`
