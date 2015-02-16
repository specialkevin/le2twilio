# le2twilio
Recieve text message whenever a logentries alert is triggered.
The message you receive is in the following format: There is an alert for <logentries alert name> on <host>.

## Installation on Heroku

### Install

    git clone https://github.com/specialkevin/le2twilio.git

### Create Heroku App

    heroku create <APP NAME>

### Setup Environment Variables

    heroku config:set RECEPIENT_PHONE_NUMBER=<PHONE NUMBER TO SEND ALERTS TO>
    heroku config:set TWILIO_PHONE_NUMBER=<YOUR TWILIO PHONE NUMBER
    heroku config:set TWILIO_ACCOUNT_SID=<TWILIO ACCOUNT SID>
    heroku config:set TWILIO_AUTH_TOKEN=<TWILIO AUTHORIZATION TOKEN>
    heroku config:set LE_WEBHOOK_PASSWORD=<LOGENTRIES WEBHOOK SHARED SECRET>

### Deploy to Heroku

    git push heroku master

### Add WebHook Alert in Logentries
