from flask import request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token

from server.DBsettings import curs, conn


def login():
    try:
        user_id = request.json['id']
        password = request.json['pw']
        user_ip = request.remote_addr
    except KeyError or TypeError:
        return jsonify({'msg': '틀린 폼'}), 400

    query_select_userinfo = 'select id, pw, name from userinfo where id = %s'
    curs.execute(query_select_userinfo, user_id)
    user_info = curs.fetchone()
    if not user_info:
        return jsonify({'msg': '없는 유저'}), 401

    if user_info['pw'] != password:
        return jsonify({'msg': '없는 유저'}), 401

    identity = {'name': user_info['name'], 'id': user_id}
    access_token = create_access_token(identity=identity)
    refresh_token = create_refresh_token(identity=identity)

    query_select_refreshtoken = 'select id from refreshtoken where id = %s'
    curs.execute(query_select_refreshtoken, user_id)
    exist = curs.fetchone()

    if exist:
        query_update_refreshtoken = 'update refreshtoken set refreshToken = %s, ip = %s where id = %s'
        curs.execute(query_update_refreshtoken, (refresh_token, user_ip, user_id))
        conn.commit()
    else:
        query_insert_refreshtoken = 'insert into refreshtoken (id, name, refreshToken, ip) values (%s, %s, %s, %s)'
        curs.execute(query_insert_refreshtoken, (user_id, user_info['name'], refresh_token, user_ip))
        conn.commit()

    return jsonify({'access': access_token}, {'refresh': refresh_token}), 200
