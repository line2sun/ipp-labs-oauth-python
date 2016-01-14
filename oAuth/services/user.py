import mongoengine

from oAuth.models import User
from .crypto import hash, are_same_hashes


def register(name, email, password):
    """ Registers an user in to the system.
    """
    instance = User(email=email, name=name)
    salt, hashed_password = hash(password)
    instance.password = hashed_password
    instance.salt = salt
    try:
        instance.save()
    except mongoengine.SaveConditionError:
        print 'Failed to save!'
        return None
    print "Successfully saved person ", email
    return instance