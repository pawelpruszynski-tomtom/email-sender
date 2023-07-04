from __future__ import print_function
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint
from util.secrets_handler import AzureSecrets


class Email:

    secret = AzureSecrets()
    API_KEY = secret.retrieve_secret("brevo-smtp-api-key").value
    HEADERS = {"Some-Custom-Name": "unique-id-1234"}
    PARAMS = {"parameter": "My param value", "subject": "New Subject"}

    def __init__(self,
                 subject,
                 html_content,
                 sender,
                 to,
                 cc=None,
                 bcc=None,
                 reply_to=None):

        self.smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to,
                                                       bcc=bcc,
                                                       cc=cc,
                                                       reply_to=reply_to,
                                                       headers=self.HEADERS,
                                                       html_content=html_content,
                                                       sender=sender,
                                                       subject=subject
                                                       )

    def send_email(self):

        configuration = sib_api_v3_sdk.Configuration()
        configuration.api_key['api-key'] = self.API_KEY

        api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))

        try:
            api_response = api_instance.send_transac_email(self.smtp_email)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)
