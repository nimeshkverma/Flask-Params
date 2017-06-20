# flask-params

Processes the Request params for Flask served as a Python library

`pip install flask-params`

### Instructions:
- Install the package
- Import the `process` decorator from flask_params
  `from flask_params.flask_params import process`
- Use the decorator for the function handling the requests
  
  ` @process(param_config,header_config)`
  
  ` def get_view1(params, header_params):` 
  
  Where `param_config` and `header_config` are the JSON Schema for the params and headers respectively.

### Pypi Page: 
https://pypi.python.org/pypi/flask_params/1.0.1
