# pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib

from google.oauth2 import service_account
from googleapiclient.discovery import build

service_account_file = 'credentails.json'
scopes = ['https://www.googleapis.com/auth/cloud-platform']

credentails = service_account.Credentials.from_service_account_file(
    service_account_file, scopes=scopes
)

service = build('iam', 'v1', credentials=credentails)

project_id = 'mytesting-400910'

service_accounts = service.projects().serviceAccounts().list(
    name=f'projects/{project_id}'
).execute()


if 'accounts' in service_accounts:
    for account in service_accounts['accounts']:
        print(f"Name: {account['name']}, Email: {account['email']}")
        
else:
    print('No service account found')

