import json

def response(request_data : bytes) -> bytes:
    print(f"Received data: {request_data}")

    try:
        json_request = json.loads(request_data)

        if not isinstance(json_request, dict):
            raise ValueError("JSON data must be a dictionary")

        numbers : list[int] = json_request['numbers']
        numbers.sort()

        json_response = {
            'numbers' : numbers
        }

        response_data = json.dumps(json_response).encode()

        return response_data

    except ValueError as e:
        print(f"Error processing JSON data: {e}")
