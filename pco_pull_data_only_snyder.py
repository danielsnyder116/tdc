#--------------------------------------------------------
# CODE TO CONNECT TO PLANNING CENTER API AND SAVE OUTPUT
#--------------------------------------------------------

#Set path in order to import module code
import os
os.chdir("/Users/dsnyder/code/tdc/")

from utils import *


# user_id = '56660542' #P
# org_id = '49547'     #O

#all possible API topics
topics = ['people', 'check-ins', 'groups', 'giving', 'services']
          
          'check-ins', 
            'publishing', 
          ]

#ones I can access for own user account
# me_topics = ['people', 'services', 'groups']


CLIENT_ID = os.getenv('TDC_ADMIN_CLIENT_ID')
SECRET = os.getenv('TDC_ADMIN_SECRET')


BASE_URL = 'https://api.planningcenteronline.com/'
ME_URL = BASE_URL + 'people/v2/me'
NOTES_URL = BASE_URL + 'people/v2/people/56660542/notes'

def get_data(url):
    """Function to handle boilerplate code for making API request
    """
    
    resp = requests.get(url, auth=(CLIENT_ID, SECRET))
    print(f"{resp}\n\n")
    print(resp.json())
    
    return resp.json()
    

ME_URL

base_json = get_data(ME_URL)['data']

notes = get_data(NOTES_URL)

df_att = pd.DataFrame(base_json['attributes']).reset_index(drop=True)
df_att.head()
# df_rel = pd.DataFrame(base_json['relationships'])
# df.head()


result = get_data(BASE_URL + 'giving/v2/giving/me')

for topic in topics:
    print(f"*****{topic}*****\n")
    try:
        result = get_data(BASE_URL + f"{topic}/v2/me")
    except Exception as e:
        print(e)


