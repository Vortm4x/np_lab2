import json
import re

def prepare() -> bytes:
    raw_input = input('Unsorted numbers:')
    str_numbers = re.split(r'\D', raw_input)
    str_numbers = list(filter(lambda s : len(s) > 0, str_numbers))  

    numbers = [int(num) for num in str_numbers]

    json_request = {
        'numbers': numbers
    }

    request_data = json.dumps(json_request).encode()
    
    return request_data


def handle(response_data : bytes) -> None:
    json_response = json.loads(response_data)
    
    numbers = json_response['numbers']

    print('Sorted numbers: ')

    for x in numbers:
        print(x, end=' ')
    print('\n')