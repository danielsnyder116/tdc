#--------------------------------------------------------
#     Get Ops Data for Scorecard
#--------------------------------------------------------
#Set path in order to import module code
# import os
# os.chdir("/Users/dsnyder/code/tdc/")

from utils import *

topic = 'people'
sub_topic = 'lists'
url = PCO_BASE_URL + f"{topic}/v2/{sub_topic}?per_page={chunk_size}"

#Limit to per_page param is 100
chunk_size = 99 
pco_lists = []

#As long as there is a new chunk, keep going
#TODO: determine if better to use total_count to then display chunks?
while True:
    
    #First call
    if not pco_lists:
        result = get_data(url)
        
        total_count = result['meta']['total_count']
        print(f"Total pco_lists: {total_count} with {chunk_size}")
    
    #Use provided link to iterate through next chunk
    #Once no more 'next' urls, we're done and break out of loop
    else:
        if 'next' in result['links'].keys():
            result = get_data(url=result['links']['next'])
        else:
            break
        
    pco_lists.append(result['data'])

df_lists = to_flat_df(pco_lists)

#Get unique list links to pull nested relationship data
rel_urls = df_lists['links_self'].to_list()

rel_urls

test = get_data(url=rel_urls[0])

test['data']['links']




# result = get_data(BASE_URL + f"{topic}/v2/")
#         initial_results.append(result)
#     except Exception as e:
#         print(e)
        
        
# root = initial_results[3]
# endpoints = list(root['data']['links'].values())


# second_results = []
# for endpoint in endpoints:
#     print(endpoint)
#     second_result = get_data(endpoint)
#     second_results.append(second_result)
    

# for num, result in enumerate(second_results):
#     print(num)
  
    
#     with open(f'groups_{num}_second_results.json', 'w') as file:
#         json.dump(result, file)
    

        
