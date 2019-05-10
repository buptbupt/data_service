# -*- coding: utf-8 -*-

from flask import jsonify


class APIResult(dict):

    def __init__(self, code, result=None, msg=None):
        self["code"] = code
        self["msg"] = msg
        self["result"] = result or {}

    def jsonify(self):
        json_resp = jsonify(**self)
        json_resp.headers['Cache-Control'] = 'no-cache'
        return json_resp

    def __call__(self, *arg, **kw):
        return self.jsonify()

