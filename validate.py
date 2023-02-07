import argparse
import os

from lxml import etree

def test_file(file_path):
    print("Now testing: " + file_path)
    parsed_file = etree.parse(file_path)
    xmlschema.assertValid(parsed_file)

parser = argparse.ArgumentParser()
parser.add_argument("schema_file", help="The XML schema file to use for validation")
parser.add_argument("test_file_or_dir", help="Either a single XML file to validate or a directory containig multiple files to test")
args = parser.parse_args()

xmlschema_doc = etree.parse(args.schema_file)
xmlschema = etree.XMLSchema(xmlschema_doc)

if os.path.isdir(args.test_file_or_dir):
    for file_name in os.listdir(args.test_file_or_dir):
        test_path = os.path.join(args.test_file_or_dir, file_name)
        test_file(test_path)
elif os.path.isfile(args.test_file_or_dir):
    test_file(args.test_file_or_dir)
else:
    print("Error: " + args.test_file_or_dir + " is no valid path or file!")
