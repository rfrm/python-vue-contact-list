from app import db

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.Text)
    lastname = db.Column(db.Text)
    birthdate = db.Column(db.Date)

    _emails = db.relationship('Email', cascade="all,delete-orphan")
    _addresses = db.relationship('Address', cascade="all,delete-orphan")
    _phone_numbers = db.relationship('PhoneNumber', cascade="all,delete-orphan")

    def update(self, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)

    @property
    def emails(self):
        return self._emails

    @emails.setter
    def emails(self, emails):
        self._emails = [Email(email=email) for email in emails]

    @property
    def addresses(self):
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        self._addresses = [Address(address=address) for address in addresses]

    @property
    def phone_numbers(self):
        return self._phone_numbers

    @phone_numbers.setter
    def phone_numbers(self, phone_numbers):
        self._phone_numbers = [PhoneNumber(phone_number=number['phone_number'],
                                           phone_type=number['phone_type']) for number in phone_numbers]


class Email(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text)
    contact_id = db.Column(db.Integer, db.ForeignKey('contact.id'))

    def __repr__(self):
        return str(self.email)


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.Text)
    contact_id = db.Column(db.Integer, db.ForeignKey('contact.id'))

    def __repr__(self):
        return str(self.address)


class PhoneNumber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.Text)
    phone_type = db.Column(db.Text)
    contact_id = db.Column(db.Integer, db.ForeignKey('contact.id'))
