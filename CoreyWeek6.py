import logging
import logstash
import sys
import time

test_logger = logging.getLogger('python-logstash-logger')
test_logger.setLevel(logging.INFO)
test_logger.addHandler(logstash.LogstashHandler('3.80.60.207', 5959, version=1))

#test_logger.error('python-logstash: test logstash error message.')
#test_logger.info('python-logstash: test logstash info message.')
#test_logger.warning('python-logstash: test logstash warning message.')

def getUser(name, password):
    if name == "Corey" and password == "password":
        test_logger.info('Successful user login')
    elif name != "Corey":
        test_logger.warning('Invalid Username')
    else:
        test_logger.error('Error: Username & password combination entered does not exist')

extra = {
    'test_string': 'python version: ' + repr(sys.version_info),
    'test_boolean': True,
    'test_dict': {'a': 1, 'b': 'c'},
    'test_float': 1.23,
    'test_integer': 126,
    'test_list': [1, 2, 3]
}

getUser("Corey", "password")

#test_logger.info('python-logstash: test extra fields', extra=extra)