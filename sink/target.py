#!/usr/bin/env python3
#
# Copyright 2020 TriggerMesh Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import boto3
import json
import logging

from cloudevents.http import from_http, to_json

from flask import Flask
from flask import request

# regionName = os.getenv('region', default='us-east-1')
db = boto3.resource('dynamodb', region_name=('us-east-1'))
table = db.Table('tmtest')

app = Flask(__name__)

@app.route('/', methods=['POST'])
def target():
	
    # create a CloudEvent
    event = from_http(request.headers, request.get_data())
    cejson = json.loads(to_json(event).decode('utf-8'))

    # Do your Transformation or Target work based on the eventype
    if event['type'] == "io.triggermesh.target.dynamodb.insert":
        logging.info("Store event in dynamodb")
        table.put_item(Item=cejson)
    elif event['type'] == "io.triggermesh.byown.dynamodb.delete":
        logging.info("Delete event type not supported yet")
    else:
        logging.warning("catch all")
        print(event)
        print(type(event))
        table.put_item(Item=cejson)

    return "", 204

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080)
