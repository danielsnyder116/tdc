#-----------------------------------
# Work with Spreadsheets
#-----------------------------------

from utils import *
from google_connect_utils import *

SHEET_ID = "1OGk1qafnCpSmkrM15q6CaqBgtOfDhGm3P1fCqMSx8DA"

#Connect to site (service) and GET request for data
#See google_connect_utils for how creds are generated
service = build("sheets", "v4", credentials=creds)


result = ( service.spreadsheets().values()
                  .get(spreadsheetId=SHEET_ID, range="A1:AU47")
                  .execute()
         )

data = result.get('values', [])
print(data)


df = pd.DataFrame(data)
df.head(300)
