from flask import Flask

app = Flask('oAuth')


from controllers import *

if __name__ == '__main__':
    app.run()
