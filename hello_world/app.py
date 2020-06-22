from flask_lambda import FlaskLambda
import json


app = FlaskLambda(__name__)

@app.route("/hello")
def index():
    data={
        "Message": "Hello World"
    }
    return (
        json.dumps(data),
        200,
        {'Content-Type': 'application/json'}
    )