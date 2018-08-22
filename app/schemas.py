import pdb
from marshmallow import Schema, fields, post_load
from app.models import Contact, Address, Email, PhoneNumber


class AddressField(fields.Field):
    def _serialize(self, value, attr, obj):
        return value.address

    def _deserialize(self, value, attr, data):
        return Address(address=value)

class EmailField(fields.Field):
    def _serialize(self, value, attr, obj):
        return value.email

    def _deserialize(self, value, attr, data):
        return Email(email=value)

class PhoneNumberField(fields.Field):
    def _serialize(self, value, attr, obj):
        return { 'phone_number': value.phone_number, 'phone_type': value.phone_type }

    def _deserialize(self, value, attr, data):
        return PhoneNumber(phone_number=value['phone_number'], phone_type=value['phone_type'])

class ContactSchema(Schema):
    id = fields.Integer()
    firstname = fields.Str()
    lastname = fields.Str()

    emails= fields.List(EmailField)
    addresses = fields.List(AddressField)
    phone_numbers = fields.List(PhoneNumberField)

    @post_load
    def make_contact(self, data):
        return Contact(**data)
