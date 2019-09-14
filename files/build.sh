#!/bin/bash
yum install -y gcc-c++ git make
curl -sL https://rpm.nodesource.com/setup_6.x | sudo -E bash -
yum install -y nodejs

git clone https://github.com/TokyoQ/bankedits.git
cd bankedits
source /tmp/.secret

rm -f config.json
cp config.template config.json
sed -i -e "s/{{consumer_key}}/$consumer_key/g" config.json
sed -i -e "s/{{consumer_secret}}/$consumer_secret/g" config.json
sed -i -e "s/{{access_token}}/$access_token/g" config.json
sed -i -e "s/{{access_token_secret}}/$access_token_secret/g" config.json

npm install
npm install -g forever

forever start anon.js