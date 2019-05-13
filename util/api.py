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

class api_wrap(object):

    def __init__(self, func):
        super(api_wrap, self).__init__()
        self._func = func
        self.__name__ = func.__name__

    def __get__(self, instance, owner):
        def wrap(*arg, **kw):
            return self._func(instance, *arg, **kw)
        wrap.__name__ = self._func.__name__
        return wrap

    def __call__(self, *arg, **kw):
        try:
            res = self._func(*arg, **kw)
            if isinstance(res, APIResult):
                return res.jsonify()
            return res
        except:
            import traceback
            return APIResult(1, msg=traceback.format_exc())