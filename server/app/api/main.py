from flask import jsonify
from flask_jwt_extended import jwt_required

from server.DBsettings import curs


@jwt_required
def mainpg():
    query_select_content = 'select * from content'
    curs.execute(query_select_content)
    contents = curs.fetchall()
    return jsonify({'posts': contents}), 200
