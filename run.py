from flask import Flask, render_template,request,jsonify
from models.user import User
from models import db
import os
from config import Config
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

migrate = Migrate(app, db)

manager = Manager(app)

manager.add_command('db', MigrateCommand)

from models import user

@app.route('/',methods=["GET","POST"])
def home():
    if request.method == "GET":
        return render_template("index.html")
    password =  request.values.get("password")
    username = request.values.get("username")
    email = request.values.get("email")
    user = User()
    user.password = password
    user.username = username
    user.email = email
    db.session.add(user)
    db.session.commit()
    results = User.query.filter_by(email=email).first()
    return jsonify({"username":results.username})


if __name__ == "__main__":
    app.run(debug=True)


