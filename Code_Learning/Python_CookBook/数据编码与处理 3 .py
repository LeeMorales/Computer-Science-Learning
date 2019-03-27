from xml.etree.ElementTree import Element
from xml.etree.ElementTree import tostring


def dict_to_xml(tag, d):
    """
    Turn a simple dict of key/value pairs into XML
    """
    elem = Element(tag)
    for key, val in d.items():
        child = Element(key)
        child.text = str(val)
        elem.append(child)
    return elem
    if __name__ == '__main__':
        r = dict_to_xml('root', {'1':'22', '3':'444'})
    print(r)
    print(tostring(r))
    r.set('_id','1234')
    print(tostring(r))
from xml.etree.ElementTree import parse, Element


def rw_xml():
    doc = parse('pred.xml')
    root = doc.getroot()
    # Remove a few elements
    root.remove(root.find('sri'))
    root.remove(root.find('cr'))
    # Insert a new element after <nm>...</nm>
    root.getchildren().index(root.find('nm'))

    e = Element('spam')
    e.text = 'This is a test'
    root.insert(2, e)
    # Write back to a file
    doc.write('newpred.xml', xml_declaration=True)



if __name__ == '__main__':
    rw_xml()
class XMLNamespaces:
    def __init__(self, **kwargs):
        self.namespaces = {}
        for name, uri in kwargs.items():
            self.register(name, uri)

    def register(self, name, uri):
        self.namespaces[name] = '{' + uri + '}'

    def __call__(self, path):
        return path.format_map(self.namespaces)


if __name__ == '__main__':
    ns = XMLNamespaces(html='http://www.w3.org/1999/xhtml')
    # doc.find(ns('content/{html}html'))
    # doc.findtext(ns('content/{html}html/{html}head/{html}title'))uu