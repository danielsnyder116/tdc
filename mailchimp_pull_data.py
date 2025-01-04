#--------------------------------------------------------
# CODE TO CONNECT TO MAILCHIMP API AND SAVE OUTPUT
#--------------------------------------------------------

from utils import *

API_KEY = os.getenv('MAIL_CHIMP_SNYDER_API_KEY')

url = 'https://us7.api.mailchimp.com/3.0/'
resp = requests.get(url, auth=('danielsnyder116', API_KEY))

#automatically evaluates to True if < 400
if resp:
    print(resp)
    
    results = resp.json()
    print(f"Available fields:\n{results.keys()}")
    
else:
    raise ValueError(f"Issue with connection: {resp}")

