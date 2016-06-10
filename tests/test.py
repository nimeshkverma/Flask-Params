from flask import Flask, request, jsonify
app = Flask(__name__)
import os
import sys

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path = [os.path.join(SCRIPT_DIR + '/../')] + sys.path

from flask_params import flask_params


test_get1_config = {
    'type': 'object',
            'properties': {
                'customerId': {'type': 'string'},
                'productId': {'type': 'string'},
                'qty': {'type': 'number'}
            },
    'required': ['customerId', 'productId', 'qty']
}


# @flask_params.process_params(param_config=test_get1_config)
@app.route('/test_get1', methods=['GET'])
def get_view1(params, header_params):
    print request
    res = {
        'results':
        {
            "params": params,
            "header_params": header_params
        }
    }
    print jsonify(res)
    return jsonify(res)


@app.route('/test_post1', methods=['POST'])
def post_view1():
    print request.form
    return jsonify({'results': request.form})


if __name__ == '__main__':
    app.run(
        host="localhost",
        port=int("8080")
    )
