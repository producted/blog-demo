#encoding: utf-8

from flask import g
from flask import Response
from flask import request
from flask import Blueprint
from flask import request, jsonify,url_for
from database.db import get_connection
import json
import os

blog_app = Blueprint('blog_app',__name__)

@blog_app.route("/blog/get-blog", methods=['GET'])
def getBlog():
    result = {
       "seq": "seq",
       "cmd": "cmd", 
       "data": {},
       "code": "0", 
       "msg": "ok"
    }
    print("start blog")
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            sql = '''
            SELECT * FROM `test_nacos`.`blog` ORDER BY `id` DESC ;          
            '''
            cursor.execute(sql)
            sqldata = cursor.fetchall()
    finally:
        connection.close()

    result['data'] = sqldata
    return jsonify(result)

@blog_app.route("/blog/add-blog", methods=['POST'])
def addBlog():
    result = {
       "seq": "seq",
       "cmd": "cmd", 
       "data": {},
       "code": "0", 
       "msg": "ok"
    }

    request_json = request.get_json()
    title = request_json.get('title', '')
    content = request_json.get('content', '')
    categories = request_json.get('categories', '')
    author = request_json.get('author', '')
    
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            sql = '''
            INSERT INTO `test_nacos`.`blog` (
            `title`,
            `content`,
            `author`,
            `type`
            )
            VALUES
            (
                "{}","{}","{}","{}"
            )         
            '''.format(title, content, author, categories)
            print(sql)
            cursor.execute(sql)
            connection.commit()
            sqldata = cursor.fetchall()
    finally:
        connection.close()

    result['data'] = sqldata
    return jsonify(result)

@blog_app.route("/blog/get-blog-by-id", methods=['GET'])
def getBlogById():
    result = {
       "seq": "seq",
       "cmd": "cmd", 
       "data": {},
       "code": "0", 
       "msg": "ok"
    }
    print("start blog")
    connection = get_connection()
    id = request.args.get("id")
    print(id)

    try:
        with connection.cursor() as cursor:
            sql = '''
            SELECT * FROM `test_nacos`.`blog` where id = '{}' ;          
            '''.format(id)
            print(sql)
            cursor.execute(sql)
            sqldata = cursor.fetchall()
    finally:
        connection.close()

    result['data'] = sqldata
    return jsonify(result)