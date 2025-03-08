#--------------------------------------------------------
# Get Ops Data for Scorecard
#--------------------------------------------------------
#Set path in order to import module code
import os
os.chdir("/Users/dsnyder/code/tdc/")

from utils import *

# org_id = '49547'     #O



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
    

        
        
        


