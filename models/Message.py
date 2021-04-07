import datetime

from models.Database import db, ma
from models.constants import MESSAGE_LENGTH, SUBJECT_LENGTH, USER_NAME_LENGTH


##### MODELS #####
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(USER_NAME_LENGTH), nullable=False)
    receiver = db.Column(db.String(USER_NAME_LENGTH), nullable=False)
    message = db.Column(db.String(MESSAGE_LENGTH), nullable=False)
    subject = db.Column(db.String(SUBJECT_LENGTH), nullable=False)
    creation_date = db.Column(
        db.DateTime, nullable=True, default=datetime.datetime.utcnow)
    read_by_receiver = db.Column(db.Boolean, default=False, nullable=True)


##### SCHEMAS #####
class MessageSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Message


# Init tweet schemas
message_schema = MessageSchema()
messages_schema = MessageSchema(many=True)
