import json
import DiscoveryDetails as dt

print(json.dumps(dt.discovery.get_collection(dt.environment_id, dt.collection_id).get_result(), indent=2))
