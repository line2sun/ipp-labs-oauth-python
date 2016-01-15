import datetime
import mongoengine

from oAuth.models import User, Client, Token
from .crypto import hash, generate_token, are_same_hashes


def register(client, name, email, password):
    """ Registers an user in to the system.
    """
    try:
        Client.objects.get(id=client)
    except mongoengine.DoesNotExist:
        return None

    user_instance = User(email=email, name=name)
    salt, hashed_password = hash(password)
    user_instance.password = hashed_password
    user_instance.salt = salt
    try:
        user_instance.save()
    except mongoengine.SaveConditionError:
        print 'Failed to save!'
        return None, 4
    except mongoengine.NotUniqueError:
        return None, 1

    print "Successfully saved person ", email

    token = generate_token()
    token_instance = Token(user=user_instance, client=client, token=token)
    try:
        token_instance.save()
    except mongoengine.SaveConditionError:
        return None, 4

    return token, 0


def login(client, email, password):
    """ Logs in an user.
    """
    try:
        client = Client.objects.get(id=client)
        db_user = User.objects.get(email=email)
    except mongoengine.DoesNotExist:
        return None, 2

    if not are_same_hashes(db_user.password, db_user.salt, password):
        return None, 2

    db_user.last_login = datetime.datetime.now()

    try:
        db_user.save()
    except mongoengine.SaveConditionError:
        return None, 4

    try:
        token_instance = Token.objects.get(client=client, user=db_user)
    except mongoengine.DoesNotExist:
        token = generate_token()
        token_instance = Token(client=client, user=db_user, token=token)
        try:
            token_instance.save()
        except mongoengine.SaveConditionError:
            return None, 4

    return token_instance.token, 0


def get_last_login(client, token, email):
    """ Returns last login time for a given user with a given email.
    """
    try:
        db_user = User.objects.get(email=email)
        db_client = Client.objects.get(id=client)
    except mongoengine.DoesNotExist:
        return None, 2

    try:
        token_instance = Token.objects.get(client=db_client, user=db_user, token=token)
    except mongoengine.DoesNotExist:
        return None, 3

    return db_user.last_login, 0
