import os
from flask import Flask, render_template, send_from_directory, url_for, request, redirect

app = Flask(__name__)


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
