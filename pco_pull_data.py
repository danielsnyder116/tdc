#--------------------------------------------------------
# CODE TO CONNECT TO PLANNING CENTER API AND SAVE OUTPUT
#--------------------------------------------------------

#Set path in order to import module code
import os
os.chdir("/Users/dsnyder/code/tdc/")

from utils import *

# org_id = '49547'     #O

#relevant API topics
topics = ['people', 'check-ins', 'groups', 'giving', 'services']

CLIENT_ID = os.getenv('TDC_ADMIN_CLIENT_ID')
SECRET = os.getenv('TDC_ADMIN_SECRET')
BASE_URL = 'https://api.planningcenteronline.com/'


def get_data(url):
    """Function to handle boilerplate code for making API request
    """
    
    resp = requests.get(url, auth=(CLIENT_ID, SECRET))
    print(f"{resp}\n\n")
    print(resp.json())
    
    return resp.json()
    


# df_att = pd.DataFrame(base_json['attributes']).reset_index(drop=True)
# df_att.head()
# df_rel = pd.DataFrame(base_json['relationships'])
# df.head()


initial_results = []

for topic in topics:
    print(f"*****{topic}*****\n")
    try:
        result = get_data(BASE_URL + f"{topic}/v2/")
        initial_results.append(result)
    except Exception as e:
        print(e)
        
        
        

        
root = initial_results[3]
endpoints = list(root['data']['links'].values())


second_results = []
for endpoint in endpoints:
    print(endpoint)
    second_result = get_data(endpoint)
    second_results.append(second_result)
    

for num, result in enumerate(second_results):
    print(num)
  
    
    with open(f'groups_{num}_second_results.json', 'w') as file:
        json.dump(result, file)
    

        
        
        


