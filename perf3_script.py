import json
import os
import pandas as pd

nodes = ['wn019', 'wn020', 'wn021', 'wn022']
data = []

for node1 in nodes:
    for node2 in nodes:
        if(os.path.exists("/home/pablo/ansible-thredds-cluster/tests/iperf_nodes/fetch" + '/' + node1 + '_' + node2)):
            with open("/home/pablo/ansible-thredds-cluster/tests/iperf_nodes/fetch" + '/' + node1 + '_' + node2) as json_file:
                bps = json.loads(json_file.read())["end"]["sum_sent"]["bits_per_second"]
            data.append({'from': node1, 'to': node2, 'Mbps': bps / 1e6 })
        else:
            data.append({'from': node1, 'to': node2, 'Mbps': 0})
            
df = pd.DataFrame.from_dict(data)
print(df)
