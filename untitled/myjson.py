import json
data='{"nirmal":"first","amal":"top"}'
y=json.loads(data)
x=json.dumps(y)
print(x)