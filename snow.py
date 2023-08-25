import requests
import json
import sys
import os 

INSTANCE_URL = "https://devsupport.service-now.com/"
USERNAME = os.environ.get('svc_itops_inf')
PASSWORD = os.environ.get('svc_itops_inf_password')
headers = {"Content-Type":"application/json","Accept":"application/json"}
sysid_url = "https://devops.service-now.com/api/now/table/sc_task?sysparm_query=request_item.cat_item%sysparm_fields=sys_id&sysparm_limit=1"
# Get SYS ID 
getsysid = requests.get(sysid_url,auth=(USERNAME, PASSWORD), headers= headers)
if getsysid.status_code == 200:
    sysid = getsysid.json()
    sysid_number = sysid['result'][0]['sys_id']
    print(f"The SYS ID is : {sysid_number}")
else:
    print(f"Failed to fetch task number. Error Status code: {getsysid.status_code}")

# Patch Sys ID number 
patch_url = f"https://devops.service-now.com/api/now/table/sc_task/{sysid_number}"
print(patch_url)

patchtask = requests.patch(patch_url, auth=(USERNAME, PASSWORD), headers=headers ,data="{\"assigned_to\":\"devops@company.com\",\"state\":\"3\",\"active\":\"false\",\"work_notes\":\" Project has been Created.\", \"comments\":\" Project has been Created. Please visit https://devops.com/ for login\"}")
if patchtask.status_code == 200:
            print("Task closed successfully!")
else:
            print(f"Failed to close task. Status code: {patchtask.status_code}")

