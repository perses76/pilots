from lxml import etree


class MyUrlResolver(etree.Resolver):
    def resolve(self, url, pub_id, context):
        print 'Resolve Start ------------------------'
        print "INPUT URL={}".format(url)
        file_name = url.split('/')[-1]
        fake_url = '/mnt/local/home/vadim/pilots/xml_resolver/' + file_name
        print 'RESOLVED URL = {}, pub_id={}'.format(fake_url, pub_id)

        with open(fake_url) as f:
            xmlstr = f.read()
        res = self.resolve_string(xmlstr, context)
        print 'Resolve END ------------------------'
        return res
        # return super(MyUrlResolver, self).resolve(fake_url, pub_id, context)


class ExceptionUrlResolver(etree.Resolver):
    def resolve(self, url, pub_id, context):
        print 'ExceptionUrlResolver- FAILD!!!!!!'
        return None


def main():
    resolver = MyUrlResolver()
    parser = etree.XMLParser()
    parser.resolvers.add(ExceptionUrlResolver())
    parser.resolvers.add(resolver)
    with open('main.xsd') as f:
        doc = etree.parse(f, parser=parser)
        print "Doc is loaded"
        schema = etree.XMLSchema(doc)
        print 'Schema is loaded: ' + str(bool(schema))

main()
print 'End!'
