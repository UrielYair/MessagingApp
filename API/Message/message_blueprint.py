from flask import Blueprint, jsonify, request
from models.Message import Message, MessageSchema, message_schema, messages_schema
from models.Database import db, ma
from flasgger import swag_from
from marshmallow import ValidationError


message_blueprint = Blueprint('message_blueprint', __name__)

##### messages #####


@ message_blueprint.route("/messages/")
@ swag_from('messages.yaml')
def tweets():
    all_messages = Message.query.all()
    return jsonify(messages_schema.dump(all_messages))


@ message_blueprint.route("/messages/", methods=['POST'])
@ swag_from('store_message.yaml')
def store_message_in_db():

    try:
        data = request.json

        # validate post inputs
        MessageSchema().load(data)

        sender = data['sender']
        receiver = data['receiver']
        message = data['message']
        subject = data['subject']

        new_message = Message(sender=sender, receiver=receiver,
                              message=message, subject=subject)

        db.session.add(new_message)
        db.session.commit()

        return message_schema.dump(new_message)

    except ValidationError as err:
        return err.messages


@ message_blueprint.route("/messages/<int:message_id>")
@ swag_from('read_message.yaml')
def read_message(message_id):
    # mark message as read
    message = Message.query.get_or_404(message_id)
    message.read_by_receiver = True
    db.session.commit()
    return message_schema.dump(message)


@ message_blueprint.route("/messages/<int:message_id>", methods=['DELETE'])
@ swag_from('message_delete.yaml')
def delete_message(message_id):
    # delete message by id
    message = Message.query.get_or_404(message_id)
    db.session.delete(message)
    db.session.commit()
    return message_schema.dump(message)
