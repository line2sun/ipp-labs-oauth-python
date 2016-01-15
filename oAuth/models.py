import datetime

from oAuth import db


class User(db.Document):
    email = db.StringField(max_length=50, required=True, unique=True )
    name = db.StringField(max_length=255)
    salt = db.StringField(max_length=128)
    password = db.StringField(max_length=255)
    last_login = db.DateTimeField()

    def __unicode__(self):
        return self.email

    def set_password(self, password):
        pass

    def __repr__(self):
        return {
            'name': self.name,
            'email': self.email,
            'salt': self.salt,
            'password': self.password,
            'last_login': self.last_login
        }


class Client(db.Document):
    name = db.StringField(max_length=255)

    def __unicode__(self):
        return self.name


class Token(db.Document):
    client = db.ReferenceField('Client')
    user = db.ReferenceField('User')
    token = db.StringField(max_length=128, required=True, unique=True)