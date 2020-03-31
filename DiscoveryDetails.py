from ibm_watson import DiscoveryV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from requests.auth import HTTPBasicAuth
from ibm_cloud_sdk_core.api_exception import ApiException


apikey = 'xxxxxxxxxxxx-xxxxxxxxxxxx-xxxxxxxxxx'
collection_id = 'xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx'
environment_id = 'xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx'


authenticator = IAMAuthenticator(apikey)
auth = HTTPBasicAuth('apikey', apikey)
discovery = DiscoveryV1(
    version='2019-04-30',
    authenticator=authenticator
)

headers = {
    'content-type': "application/json"
    }
    
discovery.set_service_url('https://gateway.watsonplatform.net/discovery/api')

training_path = "https://gateway.watsonplatform.net/discovery/api/v1/environments/" + environment_id + "/collections/" + collection_id  + "/training_data?version=2019-04-30"
