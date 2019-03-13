import os
import tempfile
import argparse
import json


parser = argparse.ArgumentParser()
parser.add_argument("--key", type=str)
parser.add_argument("--value", type=str)
args = parser.parse_args()
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
if args.key is None:
    print('input key and value')
    exit()
with open(storage_path, 'r') as test_file:
    test_file.seek(0)
    temp_load = test_file.read()
    temp_load = json.loads(temp_load)
if args.value is None:
    if type(temp_load) is dict:
        if args.key in temp_load:
            print(temp_load[args.key])
            exit()
        else:
            print(None)
            exit()
    else:
        print(None)
        exit()
if args.value:
    if type(temp_load) is dict:
        if args.key in temp_load:
            temp_load[args.key] = temp_load[args.key] + ', ' + str(args.value)
        else:
            temp_load[args.key] = args.value
    else:
        temp_load = {}
        temp_load[args.key] = args.value
elif temp_load[args.key] is None:
    print('None')
    exit()
else:
    print(temp_load[args.key])
    exit()
with open(storage_path, 'w') as test_file:
    test_file.write(json.dumps(temp_load))
