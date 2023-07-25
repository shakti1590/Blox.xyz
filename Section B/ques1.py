'Write a function to parse any valid json string into a corresponding Object, List, or Map object. Note that the integer and floating point should be arbitrary precision.'
import json
import ast
from decimal import Decimal
def json(json_string):
    def convert_to_arbitrary(obj):
        if isinstance(obj, dict):
            for key, value in obj.items():
                obj[key] = convert_to_arbitrary(value)
        elif isinstance(obj, list):
            for i, item in enumerate(obj):
                obj[i] = convert_to_arbitrary(item)
        elif isinstance(obj, str) and obj.replace(".", "").isdigit():
            try:
                return int(obj)
            except ValueError:
                return Decimal(obj)
        return obj

    parsed_data = json.loads(json_string)
    return convert_to_arbitrary(parsed_data)
