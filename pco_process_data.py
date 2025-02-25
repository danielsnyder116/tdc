#--------------------------------------------------------
# CODE TO PARSE & ORGANIZE PC DATA
#--------------------------------------------------------

#Set path in order to import module code
import os
os.chdir("/Users/dsnyder/code/tdc/")
from utils import *

CLIENT_ID = os.getenv('TDC_ADMIN_CLIENT_ID')
SECRET = os.getenv('TDC_ADMIN_SECRET')
BASE_URL = 'https://api.planningcenteronline.com/'


def get_data(url):
    """Function to handle boilerplate code for making API request
    """
    
    resp = requests.get(url, auth=(CLIENT_ID, SECRET))
    print(f"{resp}\n\n")
    # print(resp.status_code)
    
    return resp.json()
    


records = []

topic = 'check-ins'
sub_topic = 'event_times' #events
#Limit to per_page param is 100
chunk_size = 99


#As long as there is a new chunk, keep going
#TODO: determine if better to use total_count to then display chunks?
while True:
    
    #First call
    if not records:
        result = get_data(BASE_URL + f"{topic}/v2/{sub_topic}?per_page={chunk_size}")
        
        total_count = result['meta']['total_count']
        print(f"Total records: {total_count} with {chunk_size}")
    
    #Use provided link to iterate through next chunk
    #Once no more 'next' urls, we're done and break out of loop
    else:
        if 'next' in result['links'].keys():
            result = get_data(url=result['links']['next'])
        else:
            break
        
    records.append(result['data'])

df = pd.concat([pd.json_normalize(pull) for pull in records], axis=0)
df.columns = [col.replace('.', '_').replace('attributes_','') for col in df.columns]


df_now = df[df['relationships_event_period_data_id'] == '35999909']
df_recent = df[df['total_count'] > 0 ]
        
        

 