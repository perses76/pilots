from lxml import etree


class SkeletonSchemaValidator(object):
    def __init__(self, schema_doc):
        transform_node = self._get_trandform_node(schema_doc)
        base_schema = 2gt
        pass

    def assertValid(xml_doc):
        pass

def validXml(xml_file, xsd_file):
    with open(xsd_file) as f:
        xmlschema_doc = etree.parse(f)
        xmlschema_doc.xinclude()
        xmlschema = etree.XMLSchema(xmlschema_doc)
    with open(xml_file) as f:
        xml_doc = etree.parse(f)
    xmlschema.assertValid(xml_doc)
    print "PASSED!!! -----------------------------"


def main():
    with open("data.xsd") as f:
        xmlschema_doc = etree.parse(f)
    xmlschema_doc.xinclude()
    print etree.tostring(xmlschema_doc)
    validXml('common.xml', 'common.xsd')
    validXml('data.xml', 'data.xsd')

main()
print 'End!'
