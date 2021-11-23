import json

file = open('mock_data.txt', 'r')
Lines = file.readlines()

count = 0

for line in Lines:
    count += 1
    # print(f"Message {count}: {line.strip()}")

    json_string = json.dumps(line)
    print(f"Equivalent json str of input string: {json_string}")

    # print(type(json_string))
