#--------------------------------------------------------
# RELEVANT IMPORTS/CONSTANTS FOR OTHER SCRIPTS
#--------------------------------------------------------

import sys
import requests
import pandas as pd
import json
import os    #just for env vars

pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', 500)


#Get creds securely
with open("/Users/dsnyder/code/docs/pco_creds.json", "r") as file:
    creds = json.load(file)

PCO_CLIENT_ID = creds['client_id']
PCO_SECRET = creds['secret']

if PCO_CLIENT_ID is None or PCO_SECRET is None:
    raise ValueError("No ids found, check it out...")


#Constants
HOME = '/Users/dsnyder/code/tdc/'
BASE_URL = 'https://api.planningcenteronline.com/'


#Functions
def get_data(url):
    """Function to handle boilerplate code for making API request
    Returns data in json format
    """
    
    resp = requests.get(url, auth=(CLIENT_ID, SECRET))
    print(f"{resp}\n\n")
    # print(resp.status_code)
    
    return resp.json()
    

