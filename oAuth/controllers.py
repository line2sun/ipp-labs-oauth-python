from oAuth import app

import routes


@app.route(routes.USERS)
def index():
    return "Banana!"
