from ibm_watson import DiscoveryV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from requests.auth import HTTPBasicAuth
from ibm_cloud_sdk_core.api_exception import ApiException


apikey = 'E29xF0m167noCwt-6HvyUjGBrG7GGXc-GyEwehk35WU_'
collection_id = 'e0e5efd0-f21e-4b10-9970-b0a7fcb6f236'
environment_id = 'e5334501-92ee-40ea-9850-3467f21829a8'


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
