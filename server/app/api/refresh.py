from flask import request, jsonify
from flask_jwt_extended import jwt_refresh_token_required, get_jwt_identity, create_access_token

from server.DBsettings import curs


@jwt_refresh_token_required
def refresh():
    user_ip = request.remote_addr
    user_refresh_token = request.headers['Authorization'][7:]
    identity = get_jwt_identity()

    query_select_refreshtoken = 'select * from refreshtoken where id= %s'
    curs.execute(query_select_refreshtoken, identity['id'])
    present_token_info = curs.fetchone()
    present_ip = present_token_info['ip']
    present_refresh_token = present_token_info['refreshToken']

    if user_ip == present_ip:
        if user_refresh_token == present_refresh_token:
            return jsonify({'access': create_access_token(identity=identity)})
        else:
            return jsonify({'msg': '잘못된 token'}), 401
    else:
        return jsonify({'msg': '잘못된 token'}), 401
