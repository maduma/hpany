import sys, requests, json

tokenFile = 'token.txt'
hpsaServer = 'mslon001pngx.saas.hp.com'
tenantId = 725867830
entityType = 'Person'

"""
Get all records
"""
def getRecord(server, token, tenantId, entityType):
    rest = 'rest/{0}/ems/{1}'.format(tenantId, entityType)
    url = 'https://{0}/{1}'.format(server, rest)
    params = {'layout': 'Name'}
    cookies = {'LWSSO_COOKIE_KEY': token, 'TENANTID': str(tenantId)}
    r = requests.get(url, params=params, cookies=cookies)
    if r.status_code == requests.codes.ok:
        return json.loads(r.text)
    return None

"""
MAIN
"""
if len(sys.argv) == 2:
    entityType = sys.argv[1]

with open(tokenFile) as f:
    token = f.read()
    records = getRecord(hpsaServer, token, tenantId, entityType) 
    print(json.dumps(records, indent=4, sort_keys=True))
    if records:
        print('Found {0} records'.format(len(records['entities'])))
