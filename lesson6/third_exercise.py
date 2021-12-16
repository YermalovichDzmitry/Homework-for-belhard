import json
import yaml

data = {
    'age': 45,
    'name': 'Peter',
    'children': [
        {
            'age': 3,
            'name': 'Alice'
        }
    ],
    'married': True,
    'city': None
}

print(data)
data_serizlized = json.dumps(data)
print(data_serizlized)
data_derialized = json.loads(data_serizlized)
print(data_derialized)

with open("file_json.txt", "w") as f:
    json.dump(data, f)

with open("file_json.txt", "r") as f:
    data_derialized_file = json.load(f)
print(data_derialized_file)


data_serizlized_yaml = yaml.dump(data)
print(data_serizlized_yaml)
data_derialized_yaml = yaml.full_load(data_serizlized_yaml)
print(data_derialized_yaml)

with open("file_yaml.txt", "w") as f:
    yaml.dump(data, f)

with open("file_yaml.txt", "r") as f:
    data_derialized_yaml = yaml.safe_load(f)
print(data_derialized_yaml)
