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
def get_data(url: str):
    """Handling boilerplate code for making API request
    Returns data in json format
    """
    
    resp = requests.get(url, auth=(PCO_CLIENT_ID, PCO_SECRET))
    print(f"{resp}\n\n")
    # print(resp.status_code)
    
    return resp.json()


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
    
    

