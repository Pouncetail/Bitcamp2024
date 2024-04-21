from flask import Flask
from flask_cors import CORS
import json

app = Flask(__name__)
cors = CORS(app, origins='*')

@app.route("/pythonreturn", methods=['GET']) 
def users():
    return json.dumps(
            ["website text <b> a keyword </b>",
            {"word": "def", "word2": "def2", "word3": "def3"}], indent = 2
    )

if __name__ == "__main__":
    app.run(debug = True, port = 8080)
    