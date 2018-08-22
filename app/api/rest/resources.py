"""
REST API Resource Routing
http://flask-restplus.readthedocs.io
"""

import pdb

from datetime import datetime
from flask import request
from flask_restplus import Api

from app.api.rest.base import BaseResource, SecureResource
from app.api import api_rest

from ...models import db
from ...schemas import ContactSchema

@api_rest.route('/contacts')
class ContactList(BaseResource):
    def post(self):
        schema = ContactSchema()
        json_payload = request.json
        contact = schema.load(json_payload).data
        db.session.add(contact)
        db.session.commit()
        serialized = schema.dump(contact)
        return {'contact': serialized}, 201

# @api_rest.route('/contacts/<string:resource_id>')
