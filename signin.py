#!/usr/bin/python

import sys, requests

"""
Signin to HP Service Anywhere
Return auth token or None
Token is the value of cookie key LWSSO_COOKIE_KEY
"""
def signin(login, password, server):
    loginAPI = 'auth/authentication-endpoint/authenticate/login'
    url = 'https://{0}/{1}'.format(server, loginAPI)
    credential = '{{"Login": "{0}", "Password": "{1}"}}'
    data = credential.format(login, password)
    r = requests.post(url, data=data)
    if r.status_code == requests.codes.ok:
        return r.text
    return None

"""
MAIN
"""

# get credentials from cmdline
if len(sys.argv) < 3:
    sys.exit(0)
login = sys.argv[1]
password = sys.argv[2]

hpsaServer = 'mslon001pngx.saas.hp.com'
tokenFile = 'token.txt'

token = signin(login, password, hpsaServer)
if token:
    with open(tokenFile, 'w') as f:
        f.write(token)
        print('{0} updated'.format(tokenFile))
else:
    print('authenticaton failed')
