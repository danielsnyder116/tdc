#--------------------------------------------------------
# Script to Pull *ALL* Data From PCO
#--------------------------------------------------------
#Set path in order to import module code
import os
os.chdir("/Users/dsnyder/code/tdc/")

from utils import *

#relevant API topics
topics = ['people', 'check-ins', 'groups', 'giving', 'services']


    


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
    

        
        
        


