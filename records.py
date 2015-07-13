import sys, requests, json

"""
Get all records
"""

tokenFile = 'token.txt'
hpsaServer = 'mslon001pngx.saas.hp.com'
tenantId = 725867830
entityType = 'Person'

def getRecord(server, token, tenantId, entityType):
    rest = 'rest/{0}/ems/{1}'.format(tenantId, entityType)
    url = 'https://{0}/{1}'.format(server, rest)
    params = {'layout': 'Name'}
    cookies = {'LWSSO_COOKIE_KEY': token, 'TENANTID': str(tenantId)}
    req = requests.get(url, params=params, cookies=cookies)
    if req.status_code == requests.codes.ok:
        return json.loads(req.text)
    return None

"""
MAIN
"""

if len(sys.argv) == 2:
    entityType = sys.argv[1]

with open(tokenFile) as f:
    token = f.read()
    record = getRecord(hpsaServer, token, tenantId, entityType) 
    print(json.dumps(record, indent=4, sort_keys=True))
