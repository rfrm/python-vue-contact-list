"""
REST API Resource Routing
http://flask-restplus.readthedocs.io
"""

from datetime import datetime
from flask import request
from flask_restplus import Api

from app.api.rest.base import BaseResource, SecureResource
from app.api import api_rest

from ...models import Contact, db

@api_rest.route('/contacts')
class ContactList(BaseResource):
    """ Sample Resource Class """

    def post(self):
        json_payload = request.json

        contact = Contact(firstname=json_payload["firstname"], lastname=json_payload["lastname"])
        db.session.add(contact)
        db.session.commit()

        json_payload["id"] = contact.id

        return {'contact': json_payload}, 201

# @api_rest.route('/contacts/<string:resource_id>')
