'''
Created on May 17, 2016

@author: adh
'''

from jsonschema import validate
from jsonschema.exceptions import ValidationError
import json


def load_doc(doc_path):
    with open(doc_path, 'r') as f:
        doc = json.load(f)
    return doc

def validate_vxref(doc,schema):
    try:
        # validate doc against schema
        validate(doc, schema)
    except ValidationError as e:
        return e

def process_doc(doc_path,schema):
    print("Validating {}".format(doc_path))
    doc = load_doc(doc_path)

    result = validate_vxref(doc,schema)
    if result is None:
        print("... passed.")
    else:
        print result

def main():
    import glob
    import os

    schema_path = "../schema/vxref_schema_03.json"
    schema = load_doc(schema_path)

    data_dir = '../data/v03'
    for doc_path in glob.glob(os.path.join(data_dir,'*.json')):
        process_doc(doc_path,schema)

if __name__ == '__main__':
    main()
