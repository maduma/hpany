#!/usr/bin/python

import sys, urllib2, json

"""
Signin to HP Service Anywhere
Token is the value of cookie key LWSSO_COOKIE_KEY
"""

hpsaServer = 'mslon001pngx.saas.hp.com'

def signin(login, password, server):
    loginPath = 'auth/authentication-endpoint/authenticate/login'
    url = 'https://{0}/{1}'.format(server, loginPath)
    data = {'Login': login, 'Password': password}
    req = urllib2.Request(url, json.dumps(data))
    req.add_header('Content-Type', 'application/json')
    f = urllib2.urlopen(req)
    token = f.read()
    print(f.info())
    f.close()
    return token

if len(sys.argv) < 3:
    sys.exit(0)
login = sys.argv[1]
password = sys.argv[2]

token = signin(login, password, hpsaServer)
f = open('token.txt', 'w')
f.write(token)
f.close()
