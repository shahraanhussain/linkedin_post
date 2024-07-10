from lxml import etree
import json

# Example XML content
xml_content = '''
<library xmlns="http://example.com/library"
         xmlns:bk="http://example.com/books"
         xmlns:auth="http://example.com/authors">

    <bk:book>
        <bk:title>XML and Java</bk:title>
        <bk:author auth:id="1">Shahraan Hussain</bk:author>
        <bk:published>2010</bk:published>
    </bk:book>

    <bk:book>
        <bk:title>Python Programming</bk:title>
        <bk:author auth:id="2">Saad Lamjard</bk:author>
        <bk:published>2015</bk:published>
    </bk:book>

</library>
'''

class parser:
    def __init__(self,xml_content):
        # Parse XML content
        self.root = etree.fromstring(xml_content)

        # Define namespaces
        self.namespaces = {
            'default': 'http://example.com/library',
            'bk': 'http://example.com/books',
            'auth': 'http://example.com/authors'
        }

    def xpath_parser(self,author_xpath):
        output = []
        
        for author_elem in self.root.xpath(author_xpath, namespaces=self.namespaces):
            auth_dict = {}
            author_id = author_elem.get('{http://example.com/authors}id')  # Accessing attribute with namespace
            author_name = author_elem.text
            auth_dict["id"] = author_id
            auth_dict["name"] = author_name
            output.append(auth_dict)
        output_json = json.dumps(output, indent=4)
        print(output_json)

if __name__ == "__main__":
    # XPath to extract authors
    author_xpath = './bk:book/bk:author'
    extract = parser(xml_content)
    output_dict = extract.xpath_parser(author_xpath)
