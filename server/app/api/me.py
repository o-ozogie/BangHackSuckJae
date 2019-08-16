from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from server.DBsettings import curs


@jwt_required
def me():
    identity = get_jwt_identity()
    query_select_content = 'select title, content from content where id = %s'
    curs.execute(query_select_content, identity['id'])
    contents = curs.fetchall()
    return jsonify({'name': identity['name'], 'post': contents}), 200
