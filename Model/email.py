from Model import db


class Email(db.Model):
    __tablename__ = 'emails'

    print('Initialize of the email table started!')
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(4096))
    subject = db.Column(db.String(4096))
    message = db.Column(db.String(4096))
    print('Initialize of the email table finished!')

    def __init__(self, email, subject, message):
        self.email = email
        self.subject = subject
        self.message = message
