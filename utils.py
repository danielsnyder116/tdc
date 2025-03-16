#--------------------------------------------------------
# RELEVANT IMPORTS/CONSTANTS FOR OTHER SCRIPTS
#--------------------------------------------------------

import sys
import requests
import pandas as pd

import re
import json
import os    #just for env vars
from datetime import datetime, timezone

#Set Path
os.chdir("/Users/dsnyder/code/tdc/")

#TODO: ADD TYPE HINTING
# from typing import Any, Dict, List

pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', 300)


#Get creds securely
with open("/Users/dsnyder/code/docs/pco_creds.json", "r") as file:
    creds = json.load(file)
    file.close()

PCO_CLIENT_ID = creds['client_id']
PCO_SECRET = creds['secret']
PCO_ORG_ID = creds['org_id']


if None in [PCO_CLIENT_ID, PCO_SECRET, PCO_ORG_ID]:
    raise ValueError("At least 1 ID is missing, check it out...")
    
##TODO: Figure out why printing like 10 times
# else:
#     print("Credentials are good to go!")


#Constants
CODE_HOME = '/Users/dsnyder/code/tdc/'
PCO_BASE_URL = 'https://api.planningcenteronline.com/'


#Functions
def ping_api(url: str):
    """Handling boilerplate code for making API request
    Returns data in json format
    """
    
    resp = requests.get(url, auth=(PCO_CLIENT_ID, PCO_SECRET))
    print(f"{resp}\n\n")
    # print(resp.status_code)
    
    return resp.json()


def pull_data(topic='people', sub_topic='lists', chunk_size= 87):
    """Function that iterates through JSON API and pulls data
       returns a list of dictionaries
    """
    
        
    url = PCO_BASE_URL + f"{topic}/v2/{sub_topic}?per_page={chunk_size}"
    
    #Limit to per_page param is 100
    chunk_size = 87
    pco_lists = []
    
    #As long as there is a new chunk, keep going
    #TODO: determine if better to use total_count to then display chunks?
    while True:
        
        #First call
        if not pco_lists:
            result = ping_api(url)
            
            total_count = result['meta']['total_count']
            print(f"Total number of records: {total_count} with chunk size {chunk_size}")
        
        #Use provided link to iterate through next chunk
        #Once no more 'next' urls, we're done and break out of loop
        else:
            if 'next' in result['links'].keys():
                result = ping_api(url=result['links']['next'])
            else:
                break
            
        pco_lists.append(result['data'])
    
    return pco_lists



def to_flat_df(data_pulls):
    """Converting list of dicts to flattened dataframe
    """
    
    #Small enough that we're good to read into memory to check it out
    df = pd.concat([pd.json_normalize(pull) for pull in data_pulls], axis=0)
    df.columns = [col.replace('.', '_').replace('attributes_','') for col in df.columns]

    #Adding new metadata cols for our pulls
    #Z for Zulu, a.k.a UTC - making it match exactly js date format
    df['tdc_pulled_at_utc'] = re.sub('\..*$', 'Z', datetime.now(tz=timezone.utc).isoformat())

    df.head(20)
    
    return df
    
    

