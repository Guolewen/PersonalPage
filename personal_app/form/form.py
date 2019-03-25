from flask import Blueprint, json, request, jsonify
import copy
blueprint_form = Blueprint('form', __name__)

@blueprint_form.route('/guest_form', methods=["POST"])
def guest_form():
    print("data passed")
    print(request.get_json())
    # Here is about sending
    return json.dumps({'success': True}), 200, {'ContentType':'application/json'}

