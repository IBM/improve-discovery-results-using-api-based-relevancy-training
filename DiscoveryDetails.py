from requests.auth import HTTPBasicAuth
from ibm_cloud_sdk_core.api_exception import ApiException
from ibm_watson import DiscoveryV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

apikey = 'xxxxx_xxxxxxxxxxxxxxxxxxx_xxxxx'
project_id = 'xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx'
collection_id = 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxx'
url = 'https://api.xxxx.discovery.watson.cloud.ibm.com/instances/xxxxxxxxxxxx'
version = 'xxxxxxxx'


authenticator = IAMAuthenticator(apikey)
discovery = DiscoveryV2(
    version=version,
    authenticator=authenticator
)

discovery.set_service_url('https://api.xxxxx.discovery.watson.cloud.ibm.com')