from distutils.core import setup

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()


setup(name='flask_params',
      packages=['flask_params'],
      version='1.0.0',
      description='Processes the Request params for Flask served as a Python library ',
      long_description=long_description,
      author='Nimesh Kiran Verma, Rohit khatana',
      author_email='nimesh.aug11@gmail.com, rohitkhatana.khatana@gmail.com',
      url='https://github.com/nimeshkverma/Flask-Params',
      download_url='https://github.com/nimeshkverma/Flask-Params/tarball/1.0.0',
      py_modules=['flask-params'],
      install_requires=['jsonschema'],
      keywords=['ecart', 'cart', 'redis', 'E-commerce', 'webservices'],
      classifiers=[],
      )
