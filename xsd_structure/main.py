from lxml import etree


def main():
    # rebelrunner_unformatted_xml = load_xml('rebelrunner_unformatted.xml')
    # validate(rebelrunner_unformatted_xml, 'rebelrunner.xsd')
    # return

    print "Editor xml"
    editor_raw_xml = load_xml('editor_raw.xml')
    print etree.tostring(editor_raw_xml)

    print "rebelrunner_unformatted"
    rebelrunner_unformatted_xml = transform(editor_raw_xml, 'editor_cleaner.xsl', output_xsd_path='rebelrunner_unformatted.xsd')

    print "rebelrunner"
    rebelrunner_xml = transform(rebelrunner_unformatted_xml, 'formatters.xsl', output_xsd_path='rebelrunner.xsd')


    print "Footer custom block transfromation"
    footer_xpath = etree.ETXPath('//{rebelrunner.xsd}Footer')
    footer_block = footer_xpath(rebelrunner_xml)[0]
    # show_node(footer_block)
    skeleton_xml = transform(footer_block, 'footer_links.xsl', output_xsd_path='skeleton.xsd')

    return skeleton_xml


def show_node(node):
    # print dir(node.tag.text)
    print node.tag
    for child in node:
        show_node(child)


def transform(xml_doc, xslt_path, output_xsd_path=None):
    xslt = etree.XSLT(load_xml(xslt_path))
    result = xslt(xml_doc).getroot()
    print etree.tostring(result, pretty_print=True)
    print
    if output_xsd_path is not None:
        validate(result, output_xsd_path)
    return result


def validate(xml_doc, xsd_path):
    input_xsd_xml = load_xml(xsd_path)
    xsd = etree.XMLSchema(input_xsd_xml)
    xsd.assertValid(xml_doc)


def load_xml(xml_path):
    with open(xml_path) as f:
        return etree.parse(f)

main()
print 'End!'
