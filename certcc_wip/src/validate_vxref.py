'''
Created on May 17, 2016

@author: adh
'''

from jsonschema import validate
import json


def validate_vxref():
    # load doc
    doc_path = "../data/vu435052_vxref.json"
    with open(doc_path, 'r') as f:
        doc = json.load(f)

    # load schema
    schema_path = "../schema/vxref_schema.json"
    with open(schema_path, 'r') as f:
        schema = json.load(f)

    # validate doc against schema
    validate(doc, schema)

    print("Validation passed.")


def main():
    validate_vxref()

if __name__ == '__main__':
    main()
