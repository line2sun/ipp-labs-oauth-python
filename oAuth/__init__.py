from flask import Flask
from flask.ext.mongoengine import MongoEngine


app = Flask('oAuth')

app.config["MONGODB_SETTINGS"] = {'DB': "db_ipp_oauth"}
app.config["SECRET_KEY"] = "KeepThisS3cr3t"

db = MongoEngine(app)


from controllers import *


if __name__ == '__main__':
    app.run()
