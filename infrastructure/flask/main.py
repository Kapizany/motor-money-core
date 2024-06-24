import os
from dotenv import load_dotenv
from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate

from infrastructure.flask.db import db

load_dotenv()

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_CONN_STR")

db.init_app(app)
migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run(debug=True)