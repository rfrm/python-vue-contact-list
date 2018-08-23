import re
import pdb
from marshmallow import Schema, fields, validate, validates, ValidationError
from app.models import Contact, Address, Email, PhoneNumber

class PhoneNumberSchema(Schema):
    phone_type = fields.Str()
    phone_number = fields.Str(required=True)

    @validates('phone_number')
    def validate_phone_number(self, value):
        if not re.match('^[\d#*-]+$', value):
            raise ValidationError('Invalid phone number')


class ContactSchema(Schema):
    id = fields.Integer()
    firstname = fields.Str(required=True, validate=validate.Length(min=1, max=20))
    lastname = fields.Str(required=True, validate=validate.Length(min=1, max=20))
    birthdate = fields.Date(allow_none=True)

    emails = fields.List(fields.Str)
    addresses = fields.List(fields.Str)
    phone_numbers = fields.Nested(PhoneNumberSchema, many=True)
