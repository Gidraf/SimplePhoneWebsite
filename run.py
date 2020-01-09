from flask import Flask, render_template,request,jsonify
from models import db
from flask_migrate import Migrate

app = Flask(__name__)

db.init_app(app)

migrate = Migrate(app, db)

@app.route('/',methods=["GET","POST"])
def home():
    if request.method == "GET":
        return render_template("index.html")
    password =  request.form.get("password")
    return jsonify(password)


if __name__ == "__main__":
    app.run(debug=True)


