from distutils.core import setup

setup(name='flask_params',
      packages=['flask_params'],
      version='1.0.1',
      description='Processes the Request params for Flask served as a Python library ',
      author='Nimesh Kiran Verma, Rohit khatana',
      author_email='nimesh.aug11@gmail.com, rohitkhatana.khatana@gmail.com',
      url='https://github.com/nimeshkverma/Flask-Params',
      download_url='https://github.com/nimeshkverma/Flask-Params/tarball/1.0.1',
      py_modules=['flask-params'],
      install_requires=['Flask', 'jsonschema'],
      keywords=['params', 'requests', 'post', 'get', 'API', 'REST'],
      classifiers=[],
      )
