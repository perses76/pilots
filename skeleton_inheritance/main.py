from lxml import etree


def main():
    with open('case1/combo.xslt') as f:
        doc_xslt = etree.parse(f)
        transform = etree.XSLT(doc_xslt)

    with open('case1/combo.xml') as f:
        doc_xml = etree.parse(f)
        doc_xml.xinclude()
    result = transform(doc_xml)
    print result
    print 'End!'

main()
