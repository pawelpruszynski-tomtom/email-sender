from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential


class AzureSecrets:

    KEY_VAULT_NAME = "datateam-kv"

    def __init__(self):
        KVUri = f"https://{self.KEY_VAULT_NAME}.vault.azure.net"
        credential = DefaultAzureCredential()
        self.client = SecretClient(vault_url=KVUri, credential=credential)

    def retrieve_secret(self, secret_name):
        return self.client.get_secret(secret_name)
