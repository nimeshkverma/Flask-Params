import json
from functools import wraps
from flask import request
from jsonschema import validate, ValidationError, FormatChecker
from exception import ErrorMessage


def process_params(param_config=None, header_config=None, check_all_fields=True, *args, **kwargs):
    def deco(f):
        def extract_params(request):
            if request.method == 'POST':
                return request.get_json()
            else:
                return request.args

        def extract_headers(headers, config):
            required_header = {}
            all_present = True
            if config:
                for header_name, header_type in config.iteritems():
                    required_header[header_name] = headers(header_name)
                    if required_header[header_name]:
                        required_header[header_name] = header_type(
                            required_header[header_name])
                    else:
                        all_present = False
            required_header['_all_params_present_'] = all_present
            return required_header

        @wraps(f)
        def decorated_function(*args, **kwargs):
            try:
                params = extract_params(request)
                validate(params, param_config, format_checker=FormatChecker())
                if header_config:
                    header_params = extract_headers(
                        request.headers.get, header_config)
                    if not header_params.get('_all_params_present_'):
                        return incorrect_input_fields_error("invalid headers")
                    return f(params=params, header_params=header_params, *args, **kwargs)
                else:
                    return f(params=params, *args, **kwargs)
            except ValidationError as e:
                raise ErrorMessage(msg)
        return decorated_function
    return deco
