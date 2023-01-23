from lxml import etree

xmlschema_doc = etree.parse("opencost.xsd")
xmlschema = etree.XMLSchema(xmlschema_doc)

example = etree.parse("closed_access.xml")

xmlschema.assertValid(example)
