from flask import Blueprint, jsonify, redirect, request
from flask_login import login_required, current_user
from app.models import Queue, db
from app.forms.queue_form import New_Queue

queue_routes = Blueprint('queue', __name__)

#SECTION - View queues of a game
@queue_routes.route('/game/<int:gameId>/all', methods=["GET"])
@login_required
def get_all_queues(gameId):
    queues = Queue.query.filter(Queue.game_id == gameId).all()
    if queues:
        queuesobj = [queue.to_dict() for queue in queues]
        return jsonify(queuesobj)
    return jsonify({'errors': 'No queues available for game right now'}, 404)


#SECTION - Create a queue for a game
@queue_routes.route('/game/<int:gameId>/team/<int:teamId>/create', methods=["POST"])
@login_required
def make_queue(gameId, teamId):
    form = New_Queue()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        queue = Queue()
        form.populate_obj(queue)
        queue.game_id = gameId
        queue.team_id = teamId
        db.session.add(queue)
        db.session.commit()
        return jsonify(queue.to_dict())
    else:
        return jsonify(form.errors)

#SECTION - Delete a queue
@queue_routes.route('/<int:queueId>/delete', methods=["DELETE"])
@login_required
def delete_queue(queueId):
    queue = Queue.query.get(queueId)
    if queue:
        db.session.delete(queue)
        db.session.commit()
        return jsonify("Successfully deleted queue")
    else:
        return jsonify({"errors": "Queue not found"}, 404)
