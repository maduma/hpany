import requests, json

"""
Get single record
"""

tokenFile = 'token.txt'
hpsaServer = 'mslon001pngx.saas.hp.com'
tenantId = 725867830
entityType = 'Person'
accountId = 80585
layout = 'Name'

def getRecord(server, token, tenantId, entityType, entityId, layout):
    rest = 'rest/{0}/ems/Person/{1}'.format(tenantId, accountId)
    url = 'https://{0}/{1}'.format(server, rest)
    params = {'layout': layout}
    cookies = {'LWSSO_COOKIE_KEY': token, 'TENANTID': str(tenantId)}
    r = requests.get(url, params=params, cookies=cookies)
    if r.status_code == requests.codes.ok:
        return r.json()
    return None

with open(tokenFile) as f:
    token = f.read()
    record = getRecord(
		hpsaServer,
		token,
		tenantId,
		entityType,
		accountId,
		layout,
	) 
    print(json.dumps(record, indent=4, sort_keys=True))
