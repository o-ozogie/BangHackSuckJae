from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from server.DBsettings import curs, conn


@jwt_required
def post():
    identity = get_jwt_identity()

    try:
        title = request.json['title']
        content = request.json['content']
    except KeyError:
        return jsonify({'msg': 'json check'}), 400

    query_insert_content = 'insert into content (title, content, id) values (%s, %s, %s)'
    curs.execute(query_insert_content, (title, content, identity['id']))
    conn.commit()
    return jsonify({'msg': '성공'}), 200
