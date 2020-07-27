from lxml import etree as xml




template = xml.Element('t', attrib={'t-call': 'website.layout'})
print(xml.tostring(template, pretty_print=True, encoding='utf-8'))