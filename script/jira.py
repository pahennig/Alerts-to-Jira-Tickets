import requests
import json
import re

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

def jiraticket(summary, description, url, user, ip):
    desc = cleanhtml(description)
    if not ip:
      ip = 'None'
    if user is None:
      user = 'User email has not been found'
    try:
        r = requests.post('$JIRABASEURL/rest/api/2/issue/', auth=('$USER', '$PASSWORD'), json={ 'fields': {'project':{ 'key': 'MCAS' },'summary': str(summary),'description': str(desc),'issuetype': {'name': 'IT Help' }, 
        'customfield_10109': str(url), 'customfield_10107': str(user), 'customfield_10108': str(ip) }})
        print('Jira ticket has been created')
    except:
        print('Ticket could not be created correctly')
