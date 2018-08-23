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
from ...schemas import ContactSchema

@api_rest.route('/contacts')
class ContactList(BaseResource):
    def get(self):
        contacts = Contact.query.all()
        return { 'contacts': ContactSchema(many=True).dump(contacts).data }

    def post(self):
        contact = Contact(**request.json)
        db.session.add(contact)
        db.session.commit()
        return {'contact': ContactSchema().dump(contact).data }


@api_rest.route('/contacts/<string:resource_id>')
class ContactResource(BaseResource):
    def delete(self, resource_id):
        contact = Contact.query.filter(Contact.id == resource_id).first()
        db.session.delete(contact)
        db.session.commit()
        return {}

    def put(self, resource_id):
        contact = Contact.query.filter(Contact.id == resource_id).first()
        contact.update(**request.json)
        db.session.add(contact)
        db.session.commit()
        return { 'contact': ContactSchema().dump(contact).data }
