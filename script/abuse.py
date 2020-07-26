import requests
import json

# REST API Manipulation from Abuseipdb to see the IP type, and check if it's been reported.
def repotedIP(ip):

    token = {'Key': '$Abuseipdb TOKEN HERE'}
    x = requests.get('https://api.abuseipdb.com/api/v2/check?ipAddress=' + str(ip) + '&maxAgeInDays=90', headers=token)
    data = x.json()
    alldetails = json.dumps(data)
    resp = json.loads(alldetails)
    print('The IP ' + str(ip) + ' was reported ' + str(resp['data']['totalReports']) + ' times within 90 days')
    print('Country code: ' + str(resp['data']['countryCode']) + ' - Usage Type: ' + str(resp['data']['usageType']) + ' - ISP: ' + str(resp['data']['isp']) + '\n')
    return 'The IP ' + str(ip) + ' was reported ' + str(resp['data']['totalReports']) + ' times within 90 days\nCountry code: ' + str(resp['data']['countryCode']) + ' - Usage Type: ' + str(resp['data']['usageType']) + ' - ISP: ' + str(resp['data']['isp']) + '\n'
