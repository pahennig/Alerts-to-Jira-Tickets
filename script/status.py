__author__ = ['[Paulo Hennig](https://github.com/pahennig/)']
__version__ = '0.1'
import requests
from datetime import datetime
import time
import json
import re
import sys
import filter
import abuse
import jira

# Fetching alerts from Microsoft Cloud App Security
def tenanturl(tenant, token):
    request_data = filter.definingFilter()
    pattern = '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

    requesttotenant = requests.post(tenant, headers=token, json=request_data)

    data = requesttotenant.json()
    alldetails = json.dumps(data)
    resp = json.loads(alldetails)

    counter = 0
    while counter < len(resp['data']):
        try:
            print('[*] Alert ' + str(counter + 1))
            readablets = resp['data'][counter]['timestamp']
            print('Date: ' + time.strftime('%m/%d/%Y %H:%M:%S', time.gmtime(int(readablets) / 1000.)))

            print('Title: ' + resp['data'][counter]['title'])
            print('Description: ' + resp['data'][counter]['description'])
            print('URL: ' + resp['data'][counter]['URL'])

            # Filter for the user's email
            match = re.findall(r'[\w\.-]+@[\w\.-]+', resp['data'][counter]['description'])
            if match:
                matchuser = str(', '.join(match))
                print('Affected User: '+matchuser)
            else:
                matchuser = 'User has not been found'
            
            finalip = re.findall(pattern, resp['data'][counter]['description'])
            results = None

            if finalip:
                print('IPs registered: ' + str(finalip) + '\n')
                for i in finalip:
                    abuse.repotedIP(i)
                    if not results:
                        results = str(abuse.repotedIP(i))
                    else: 
                        results+=str(abuse.repotedIP(i))
            else:
                finalip = None

            jira.jiraticket(str(resp['data'][counter]['title']), str(resp['data'][counter]['description']), str(resp['data'][counter]['URL']), str(matchuser), str(results))

            print('\n')
            counter += 1
        except KeyboardInterrupt:
            print('Exiting...')
            sys.exit()
        except:
            print('Could not fetch alert')
            counter += 1
            pass
    
def choices():
    # Tenant Name and token
    tenant1 = '$URL HERE'
    tenant1_token = {
        'Authorization': 'Token $MCAS TOKEN HERE'}
    
    ## Specify other tenants
    # tenant2 = 'https://xxxx.us3.portal.cloudappsecurity.com/api/v1/alerts/'
    # tenant2_token = {
    #     'Authorization': 'Token $Token_HERE'}

    # Use this area to specify additional tenants. For this example, I'm using a single one
    if len(sys.argv) > 1:
        UserInput = str(sys.argv[1])
        if UserInput.lower() == 'maintenant':
            print('Tenant: 1\n')
            tenanturl(tenant1, tenant1_token)
    else:
        print('Tenant: 1\n')
        tenanturl(tenant1, tenant1_token)      

def main():
    choices()

if __name__ == '__main__':
    main()
