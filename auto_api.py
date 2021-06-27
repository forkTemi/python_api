# coding:utf-8
'''
   program: auto_api.py
   author: temi
'''
import sys
from flask import Flask, render_template, request,jsonify
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired, BadSignature
import os
import json
from public import *
from config import *
from cmd_map import *




app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

# token生成函数
@app.route('/auto_api/token', methods=["POST"])
def generate_token():
    auth_info = {'code':1,'msg':'no token to auth,please check again !','token':None}
    expiration = 60
    from_data = request.get_data()
    dict_data = json.loads(from_data)
    if not dict_data.__contains__('api_key') or dict_data.get('api_key') not in api_authkey:
        return jsonify(auth_info)
    api_key = dict_data.get('api_key')
    s = Serializer(SECRET_KEY, expires_in=expiration)
    return jsonify({"token": s.dumps({'token': api_key}).decode('ascii')})

#token验证装饰器
def verify_token(func):
    def wrapper(*args,**kwargs):
        try:
            token = request.headers["token"]
        except Exception:
            return json.dumps({'code':1,'msg':'no token to auth,please check again !','token':None})
        try:
            s = Serializer(SECRET_KEY)
            data = s.loads(token)
            res = func(*args,**kwargs)
            return  res
        except Exception:
            return jsonify({'code':1,'msg':'token auth failed,please get token retry'})
    return wrapper


@app.route('/auto_api', methods=["POST"])
@verify_token
def auto_api():
    '''
        "prc_cmd ":"",
        "value":"[]"

    :return: 
    '''
    # 传入的参数为bytes类型，需要转化成字典
    try:
        from_data = json.loads(request.get_data())
    except Exception as e:
        return jsonify({'msg':'param was not correct'})
    # 进行参数合法判断
    if from_data.__contains__('prc_cmd') and from_data.__contains__('value'):
        json_content = execute_fun(from_data.get('prc_cmd'))
    else:
        json_content = {
            'code': 0,
            'msg': 'fail',
            'data': 'Parameter pass in error'
        }
    return jsonify(json_content)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='9991')
