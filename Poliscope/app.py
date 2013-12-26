import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

# initialization
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///Poliscope'
db = SQLAlchemy(app)
app.config.update(
    DEBUG = True,
)

# controllers
@app.route("/")
def hello():
    return "Hello from Python!"

# launch
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
