from flask import request, jsonify

from server.DBsettings import curs, conn


def signup():
    try:
        user_name = request.json['name']
        user_age = int(request.json['age'])
        user_id = request.json['id']
        password = request.json['pw']
    except TypeError:
        return jsonify({'msg': '틀린 폼'}), 400

    query_select_userinfo = 'select id from userinfo where id = %s'
    curs.execute(query_select_userinfo, user_id)
    present_id = curs.fetchone()
    if present_id:
        return jsonify({'msg': '있는 유저'}), 409

    query_insert_userinfo = 'insert into userinfo (name, age, id, pw) values (%s, %s, %s, %s)'
    curs.execute(query_insert_userinfo, (user_name, user_age, user_id, password))
    conn.commit()
    return jsonify({'msg': '성공'}), 200
