from dnacentersdk import api
import pprint
import requests.packages.urllib3
import config
from netmiko import ConnectHandler
import pprint
import csv
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import os
now = datetime.now()
#current_time = now.strftime("%B:%d:%Y %H:%M:%S")
current_date = now.strftime("%B:%d:%Y")
print("Current Date =", current_date)

requests.packages.urllib3.disable_warnings()

dnac = api.DNACenterAPI(username=config.username,
                        password=config.password,
                        base_url=config.base_url,
                        version='2.1.2',
                        verify=False,
                        single_request_timeout=99999,
                        debug=False)

print("Getting token ...")
print("Pulling devices information ...")
issues_info = dnac.issues.issues()
print(issues_info)

issue_data = {'Issue_description': [], 'Issue Occurence': [], 'Status': [], 'Priority': [],
              'Issue_occurence_count': []}

for issue in issues_info['response']:

    issue_data['Issue_description'].append(issue['name'])
    issue_data['Status'].append(issue['status'])
    issue_data['Priority'].append(issue['priority'])
    issue_data['Issue_occurence_count'].append(issue['issue_occurence_count'])
    # add date and check priority


df = pd.DataFrame(issue_data, columns=['Issue_description', 'Status', 'Priority', 'Issue_occurence_count'])
print(df)
#df.to_csv('issues_data.csv', index=False, header=True)
output_file = 'Americas_issues_data_ ' + current_date + '.csv'
dir_path = 'Output'

if not os.path.exists(dir_path):
    os.mkdir(dir_path)
df.to_csv(dir_path + '/' + output_file)








#df.to_csv('MacAddress_data.txt', index=False)
'''
interface_info = {'Hostname': [], 'Portname': [], 'Series': [], 'Description': [], 'MacAddress':[], 'ProductId':[]}
for device in switches['response']:

    try:

        servers = dnac.devices.get_interface_info_by_id(device_id=device['id'])

        for server in servers['response']:

            print('Printing server portname, series, desc, Mac address and pid')
            print(device['hostname'] + server['portName'] + '   ' + server['series'] + '   ' + server['description']
                  + '   ' + server['macAddress'] + '   ' + server['pid'])
            interface_info['Hostname'].append(device['hostname'])
            interface_info['Portname'].append(server['portName'])
            interface_info['Series'].append(server['series'])
            interface_info['Description'].append(server['description'])
            interface_info['MacAddress'].append(server['macAddress'])
            interface_info['ProductId'].append(server['pid'])


    except:
        continue

df = pd.DataFrame(interface_info, columns= ['Hostname', 'Portname', 'Series', 'Description', 'MacAddress','ProductId'])

print (df)
df.to_csv('apac_data.csv', index = False, header=True)
df.to_csv(('apac_data.txt'), index=False, header=True)
'''