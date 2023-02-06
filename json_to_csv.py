import json
import pandas as pd


f = open('file.json')
data = json.load(f)
offering_ids = []

for offering in data['data']['offerings']:
    # Append to the list
    offering_ids.append(offering['OfferingID'])

df = pd.DataFrame({'Offering_ids': offering_ids, 'System': "constant"})
#df2 = df.to_string(index=False)

#print(df)

df.to_csv("offering_id.csv", index=False)
