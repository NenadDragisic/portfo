import os
from flask import Flask, render_template, send_from_directory, request, redirect
import Model
from Model import email


def create_app(db):
    app = Flask(__name__)
    print('Created flask app context.')
    db.init_app(app)
    print('Initiated db using app context.')
    return app


if __name__ == 'server':
    print('Entered app initialization!')
    app = create_app(Model.db)

print('Getting username and password.')
username = os.environ.get('DB_USER')
password = os.environ.get('DB_PASS')
print('Username and password fetched.')

print('Setting database connection string parameters.')
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username=username,
    password=password,
    hostname="NenadD.mysql.pythonanywhere-services.com",
    databasename="NenadD$portfodb",
)
print('Database connection string parameters configured.')

print('Configuring app config.')
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
print('App config configured.')

print('Getting app context.')
with app.app_context():
    print('Creating database.')
    Model.db.create_all()
    Model.db.session.commit()
print('Database created.')

@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def get_page(page_name):
    return render_template(page_name + '.html')


@app.route('/send_email', methods=['POST', 'GET'])
def login():
    print(f'method hit, request type: {request.method}')
    error = None
    if request.method == 'POST':
        print(f"Email: {request.form['email']}")
        email = request.form['email']
        print(f"Content: {request.form['content']}")
        content = request.form['content']
        print(f"Subject: {request.form['subject']}")
        subject = request.form['subject']
    print('yolo!')
    return redirect('/email_sent_notification')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico')
