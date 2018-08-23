import pdb
from marshmallow import Schema, fields, post_load
from app.models import Contact, Address, Email, PhoneNumber


class AddressSchema(Schema):
    address = fields.Str()

class EmailSchema(Schema):
    email = fields.Str()

class PhoneNumberSchema(Schema):
    phone_number = fields.Str()
    phone_type = fields.Str()

class ContactSchema(Schema):
    id = fields.Integer()
    firstname = fields.Str()
    lastname = fields.Str()
    birthdate = fields.Date()

    phone_numbers = fields.Nested(PhoneNumberSchema, many=True)
    emails = fields.Nested(EmailSchema, only="email", many=True)
    addresses = fields.Nested(AddressSchema, only="address", many=True)
