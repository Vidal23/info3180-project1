from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "$ecretey"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:xymmuzwmirhslv:12dbac9d4e64c97779b533e9bf72b6c0bfc334fa3c9cb8f1f641648eadf52dde@ec2-54-163-246-193.compute-1.amazonaws.com:5432/da9f1r2m13sov4'"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
app.config['UPLOAD_FOLDER'] = "./app/static/uploads"

db = SQLAlchemy(app)


app.config.from_object(__name__)
from app import views
