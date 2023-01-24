import argparse

from lxml import etree

parser = argparse.ArgumentParser()
parser.add_argument("schema_file", help="The XML schema file to use for validation")
parser.add_argument("test_file", help="The XML file to validate")
args = parser.parse_args()

xmlschema_doc = etree.parse(args.schema_file)
xmlschema = etree.XMLSchema(xmlschema_doc)

example = etree.parse(args.test_file)

xmlschema.assertValid(example)
