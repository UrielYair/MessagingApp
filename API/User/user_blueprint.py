from flask import Blueprint, jsonify, request

from models.Message import Message, MessageSchema, message_schema, messages_schema
from models.Database import db, ma

from flasgger import swag_from

user_blueprint = Blueprint('user_blueprint', __name__)


##### users #####

@ user_blueprint.route("/users/<string:username>/messages/")
@ swag_from('user_messages.yaml')
def get_all_messages_by_username(username):

    # get all the messages from the DB by username - check in sender or receiver
    all_messages = Message.query.filter(
        ((Message.sender == username) | (Message.receiver == username))
    ).all()

    return jsonify(messages_schema.dump(all_messages))


@ user_blueprint.route("/users/<string:username>/messages/unread")
@ swag_from('user_unread_messages.yaml')
def get_unread_messages_for_specific_username(username):

    # get all the messages that the user not yet read
    all_unread_messages = Message.query.filter(
        db.and_(Message.receiver == username,
                Message.read_by_receiver == False)
    ).all()

    return jsonify(messages_schema.dump(all_unread_messages))
