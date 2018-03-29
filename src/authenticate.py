import uuid
import server
import pymonzo
from ConfigParser import ConfigParser


# Setup PyMonzo to be the correct redirect url
pymonzo.monzo_api.config.PYMONZO_REDIRECT_URI = 'http://127.0.0.1:8080/monzo/auth'
pymonzo.monzo_api.config.REDIRECT_URI = 'http://127.0.0.1:8080/monzo/auth'

# Read the api_info.conf
conf = ConfigParser()
conf.read('api_info.conf')
data = dict(conf.items('monzo'))

# Build up the URL to get the token
url = 'https://auth.getmondo.co.uk/?client_id={}&response_type=code&redirect_uri={}&state={}'
redirect_url = pymonzo.monzo_api.config.PYMONZO_REDIRECT_URI
state = uuid.uuid4()
state = '{}'.format(state)
print url.format(data['client_id'], redirect_url, state)

# Wait for the server to respond
httpd = server.run(port=8080, serve=False)
httpd.serve_forever(poll_interval=0.5)

# Check that the server.state and state_id are the same. If they aren't, abort!
if server.state != state:
    print 'States don\'t match :( aborting.'
else:
    # Setup authenticating using the auth_code
    data['auth_code'] = server.code
    api = pymonzo.MonzoAPI(client_id=data['client_id'], client_secret=data['client_secret'], auth_code=data['auth_code'])

    # Show whoami() to prove we have authenticated correctly.
    print api.whoami()
