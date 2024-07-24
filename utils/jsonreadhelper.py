import json

from jsonschema.protocols import Validator
from jsonschema import validate, Draft7Validator

class Json_reader:

    @staticmethod
    def get_schema(schema):
        with open(schema,'r') as file:
            schema = json.load(file)
            return schema

    @staticmethod
    def validate_schema(json_data, schema):
        schema = Json_reader.get_schema(schema)
        return validate(instance=json_data, schema=schema)
