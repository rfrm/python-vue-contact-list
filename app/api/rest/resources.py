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

from ...models import Contact, db
from ...schemas import ContactSchema, ValidationError

@api_rest.route('/contacts')
class ContactList(BaseResource):
    def get(self):
        contacts = Contact.query.all()
        return { 'contacts': ContactSchema(many=True).dump(contacts) }

    def post(self):
        try:
            ContactSchema().load(request.json)
            contact = Contact(**request.json)
            db.session.add(contact)
            db.session.commit()
            return {'contact': ContactSchema().dump(contact) }
        except ValidationError as e:
            return {'errors': str(e)}, 422

@api_rest.route('/contacts/<string:resource_id>')
class ContactResource(BaseResource):
    def delete(self, resource_id):
        contact = Contact.query.filter(Contact.id == resource_id).first()
        db.session.delete(contact)
        db.session.commit()
        return {}

    def put(self, resource_id):
        try:
            ContactSchema().load(request.json)
            contact = Contact.query.filter(Contact.id == resource_id).first()
            contact.update(**request.json)
            db.session.add(contact)
            db.session.commit()
            return { 'contact': ContactSchema().dump(contact) }
        except ValidationError as e:
            return {'errors': str(e)}, 422
