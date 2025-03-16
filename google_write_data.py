#----------------------------------------------------
# Google Boilerplate to write data to Google Drive
#----------------------------------------------------

from google_connect_utils import *
os.chdir('/Users/dsnyder/code/tdc')


from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

service.files()

test


requests.post(url="https://www.googleapis.com/upload/drive/v3/files?uploadType=media",
              json=,   )


def upload_basic(file_name):
  """Insert new file.
  Returns : Id's of the file uploaded

  Load pre-authorized user credentials from the environment.
  TODO(developer) - See https://developers.google.com/identity
  for guides on implementing OAuth2 for the application.
  """

  try:
    # create drive api client
    service = build("drive", "v3", credentials=creds)

    file_metadata = {"name": f"{file_name}.json"}
    media = MediaFileUpload(f"{file_name}.json", mimetype="application/json")
    # pylint: disable=maybe-no-member
    file = (
        service.files()
        .create(body=file_metadata, media_body=media, fields="id")
        .execute()
    )
    print(f'File ID: {file.get("id")}')

  except HttpError as error:
    print(f"An error occurred: {error}")
    file = None

  return file.get("id")



upload_basic('')