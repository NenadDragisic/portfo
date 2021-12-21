from Model import db


class Email(db.Model):
    __tablename__ = 'emails'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(4096))
    subject = db.Column(db.String(4096))
    message = db.Column(db.String(4096))