from app import db

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.Text)
    lastname = db.Column(db.Text)

    emails = db.relationship('Email', cascade="all,delete-orphan")
    addresses = db.relationship('Address', cascade="all,delete-orphan")
    phone_numbers = db.relationship('PhoneNumber', cascade="all,delete-orphan")


class Email(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text)
    contact_id = db.Column(db.Integer, db.ForeignKey('contact.id'))


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.Text)
    contact_id = db.Column(db.Integer, db.ForeignKey('contact.id'))


class PhoneNumber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.Text)
    phone_type = db.Column(db.Text)
    contact_id = db.Column(db.Integer, db.ForeignKey('contact.id'))
