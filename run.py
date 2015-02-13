#!/usr/bin/env python

import os
import hmac
import hashlib
import base64
import json

from flask import Flask, request, abort

from twilio.rest import TwilioRestClient

app = Flask(__name__)
app.debug = os.environ.get('DEBUG') == 'true'

@app.route("/", methods=['POST'])
def index():
  #content_md5 = base64.b64encode(hashlib.md5(content).digest)
  content_md5 = request.headers.get('Content-Md5')
  canonical = '\n'.join(['POST', request.headers.get('Content-Type'),
                          content_md5, request.headers.get('Date'),
                          request.path, request.headers.get('X-Le-Nonce')])

  signature = base64.b64encode(hmac.new(os.environ.get('LE_WEBHOOK_PASSWORD'), canonical, hashlib.sha1).digest())

  if signature == request.headers.get('Authorization').split(':')[1]:
    print "Succeful Alert"
    payload = json.loads(request.form['payload'])

    alert_name = payload['alert']['name']
    alert_host = payload['host']['name']

    message_body = "There is an alert for {alert_name} on {alert_host}.".format(alert_name=alert_name, alert_host=alert_host)

    send_sms(message_body)

    return "OK"
  else:
    print "Bad Authorization"
    abort(403)


def send_sms(message_body):
    client = TwilioRestClient()
    to_number = os.environ['RECEPIENT_PHONE_NUMBER']
    from_number = os.environ['TWILIO_PHONE_NUMBER']
    client.sms.messages.create(to=to_number,
                                from_=from_number, body=message_body)
    return


if __name__ == "__main__":
  port = int(os.environ.get("PORT", 5000))
  app.run(host='0.0.0.0', port=port)
