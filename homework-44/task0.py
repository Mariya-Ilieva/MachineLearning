import sys
import json
import pandas as pd
from lxml import objectify


obj = """
{"name": "Wes",
 "cities_lived": ["Akron", "Nashville", "New York", "San Francisco"],
 "pet": null,
 "siblings": [{"name": "Scott", "age": 34, "hobbies": ["guitars", "soccer"]},
 {"name": "Katie", "age": 42, "hobbies": ["diving", "art"]}]
}
"""
result = json.loads(obj)
print(result)

asjson = json.dumps(result)
print(asjson)

siblings = pd.DataFrame(result['siblings'], columns=['name', 'age'])
print(siblings)

data = pd.read_json('example.json')
print(data)
print(data.to_json(sys.stdout))
print(data.to_json(sys.stdout, orient='records'))

tables = pd.read_html('fdic_failed_bank_list.html')
print(len(tables))

failures = tables[0]
print(failures.head())

close_timestamps = pd.to_datetime(failures['Closing Date'])
print(close_timestamps.dt.year.value_counts())

path = 'Performance_MNR.xml'
with open(path) as f:
    parsed = objectify.parse(f)

root = parsed.getroot()

data = []
skip_fields = ['PARENT_SEQ', 'INDICATOR_SEQ', 'DESIRED_CHANGE', 'DECIMAL_PLACES']

for elt in root.INDICATOR:
    el_data = {}

    for child in elt.getchildren():
        if child.tag in skip_fields:
            continue

        el_data[child.tag] = child.pyval

    data.append(el_data)

perf = pd.DataFrame(data)
print(perf.head())

perf2 = pd.read_xml(path)
print(perf2.head())

frame = pd.read_csv('ex1.csv')
print(frame)

print(frame.to_pickle('frame_pickle.pkl'))
print(pd.read_pickle('frame_pickle.pkl'))
