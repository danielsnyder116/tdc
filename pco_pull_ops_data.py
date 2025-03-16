#--------------------------------------------------------
#     Get Ops Data for Scorecard
#--------------------------------------------------------
#Set path in order to import module code
import os
os.chdir("/Users/dsnyder/code/tdc/")
from utils import *


# A. MISSION FORCE CALCULATION METRICS
#------------------------------------


mission_force_info = pull_data(topic='people', sub_topic='lists')
type(mission_force_info[0][0])

test = json.dumps(mission_force_info)
















#Transformations to convert to spreadsheet format (ss)
df_lists = to_flat_df(mission_force_info)
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


df_lists['list_name']

#FILL IN SPREADSHEET





# #Don't actually need this at the moment, just the total stat
# #Get unique list links to pull nested relationship data
# rel_urls = df_lists['links_self'].to_list()
# rel_urls
# test = get_data(url=rel_urls[0])
# test['data']['links']
