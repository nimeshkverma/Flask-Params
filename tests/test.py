from flask import Flask, request, jsonify
app = Flask(__name__)
import os
import sys

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path = [os.path.join(SCRIPT_DIR + '/../')] + sys.path

from flask_params import request_params


test_get1_config = {
    'type': 'object',
            'properties': {
                'categoryId': {'type': 'string'},
                'productId': {'type': 'number'}
            },
    'required': ['categoryId']
}


@app.route('/test_get1', methods=['GET'])
@request_params(param_config=test_get1_config)
def get_view1(params):
    print params
    res = {
        'results':
        {
            "params": params,
            "header_params": "header_params"
        }
    }
    print jsonify(res)
    return jsonify(res)
    # return "Hello"


@app.route('/test_post1', methods=['POST'])
def post_view1():
    print request.form
    return jsonify({'results': request.form})


if __name__ == '__main__':
    print 1
    app.config['DEBUG'] = True
    app.run()


class A(object):

    def __init__(self):
        self.b = 1000

    def a(self):
        self.b += 1
        return self

    def c(self):
        self.b += 17
        return self
