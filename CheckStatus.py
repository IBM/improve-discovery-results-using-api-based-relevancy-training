import json
import DiscoveryDetails as dt

print(json.dumps(dt.discovery.get_project(project_id=dt.project_id).get_result(), indent=2))
