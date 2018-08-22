from app import db

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.Text)
    lastname = db.Column(db.Text)


class Email(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text)
    contact_id = db.Column(db.Integer, db.ForeignKey('contact.id'))
    contact = db.relationship('Contact',
            single_parent=True,
            backref=db.backref('emails'),
            cascade="all, delete-orphan")


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.Text)
    contact_id = db.Column(db.Integer, db.ForeignKey('contact.id'))
    contact = db.relationship('Contact',
            single_parent=True,
            backref=db.backref('addresses'),
            cascade="all, delete-orphan")


class PhoneNumber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.Text)
    phone_type = db.Column(db.Text)
    contact_id = db.Column(db.Integer, db.ForeignKey('contact.id'))
    contact = db.relationship('Contact',
            single_parent=True,
            backref=db.backref('phone_numbers'),
            cascade="all, delete-orphan")
