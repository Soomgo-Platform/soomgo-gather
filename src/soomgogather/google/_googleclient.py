import google.auth
from google.oauth2 import service_account
from googleapiclient.discovery import build


class BaseGoogleClient:
    def __init__(self, key_file=None):
        if key_file is None:
            self.credential = self.create_credential_default()
        else:
            self.credential = self.create_credential_from_file(key_file)
        self.service = self.create_service()

    def create_credential_from_file(self, key_file):
        credential = service_account.Credentials.from_service_account_file(key_file, scopes=self.scope)

        return credential

    def create_credential_default(self):
        credential, project = google.auth.default(scopes=self.scope)

        return credential

    def create_service(self):

        service = build(self.service_name, self.service_version, credentials=self.credential)

        return service
