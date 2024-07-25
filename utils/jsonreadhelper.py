import json
from utils.generate_logs import Loggen
from jsonschema.protocols import Validator
from jsonschema import validate, Draft7Validator

class Json_reader:


    @staticmethod
    def validate_schema(json_file_name,response_data):
        """Validates response data against a JSON schema and logs the results."""
        logs = Loggen.logger()
        file_path = f"/Users/user/PycharmProjects/API_personal_framework/piyush_apis_framework/schema/{json_file_name}"
        with open(file_path, 'r') as schema_file:
            logs.info(f"taking a file from schema file name is {json_file_name}")
            schema = json.load(schema_file)
        try:
            validate(instance=response_data, schema=schema)
            logs.info(f"Validation is successful")
        except Exception as E:
            logs.error("Validation is Unsucessful: ", E)




