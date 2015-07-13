import urllib2, json

"""
"""

tokenFile = 'token.txt'
hpsaServer = 'mslon001pngx.saas.hp.com'
tenantId = 725867830
accountId = 80585

def getPersonRecord(server, token, tenantId, accountId):
    rest = 'rest/{0}/ems/User?layout=Id'.format(tenantId, accountId)
    url = 'https://{0}/{1}'.format(server, rest)
    print(url)
    req = urllib2.Request(url)
    req.add_header('Accept', 'application/json')
    cookie = 'LWSSO_COOKIE_KEY={0}'.format(token)
    print(cookie)
    req.add_header('Cookie', cookie)
    print(req)
    f = urllib2.urlopen(req)
    token = f.read()
    print(token)
    f.close()

with open(tokenFile) as f:
    token = f.read()
    getPersonRecord(hpsaServer, token, tenantId, accountId)
