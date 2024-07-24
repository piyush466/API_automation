import json

from jsonschema.protocols import Validator
from jsonschema import validate, Draft7Validator

class Json_reader:

    @staticmethod
    def validate_schema(json_file_name,response_data):
        file_path = f"/Users/user/PycharmProjects/API_personal_framework/piyush_apis_framework/schema/{json_file_name}"
        with open(file_path, 'r') as schema_file:

            schema = json.load(schema_file)
        try:
            validate(instance=response_data, schema=schema)
            print("Validation succesfull")
        except Exception as E:
            print("validation Unsuccesfull", E)

