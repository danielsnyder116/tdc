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


#Transformations to convert to spreadsheet format (ss)
df_lists = to_flat_df(pco_lists)
df_lists = ( df_lists[['name', 'updated_at',
                       'total_people', 'tdc_pulled_at_utc']]
                    .rename(columns={'name':'list_name',
                                     'updated_at':'date'}) 
                    .sort_values('list_name')
                    .reset_index(drop=True)
            )

df_lists['date'] = pd.to_datetime(df_lists['date']).dt.date
df_lists = df_lists[df_lists['list_name'].str.contains('Mission.*')]

#PIVOT!
df_ss = df_lists.pivot(index='date', columns='list_name', values='total_people')



#FILL IN SPREADSHEET








# #Don't actually need this at the moment, just the total stat
# #Get unique list links to pull nested relationship data
# rel_urls = df_lists['links_self'].to_list()
# rel_urls
# test = get_data(url=rel_urls[0])
# test['data']['links']
