#-----------------------------------
# Generate & Load GOOGLE Creds
#-----------------------------------

#Installing needed google api packages
# !pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

#List of scopes
# https://developers.google.com/sheets/api/scopes

from utils import *
os.chdir("./../docs")

import google.auth
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


#Access/permissions
SCOPES = ['https://www.googleapis.com/auth/drive',
          'https://www.googleapis.com/auth/spreadsheets']


#BOLIERPLATE CODE FOR CREDENTIALS
creds = None

# The file token.json stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first time.
if os.path.exists("google_token.json"):
  creds = Credentials.from_authorized_user_file("google_token.json", SCOPES)
  
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
  if creds and creds.expired and creds.refresh_token:
    creds.refresh(Request())
  else:
    flow = InstalledAppFlow.from_client_secrets_file("google_api_snyder_credentials.json", SCOPES)
    creds = flow.run_local_server(port=0)
    
  # Save the credentials for the next run
  with open("google_token.json", "w") as token:
    token.write(creds.to_json())
    