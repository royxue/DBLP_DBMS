"""
Extract Data from XML and export to MySQL
"""
import xml.sax
from publication import Publication
from db import DB


class DBLPHandler(xml.sax.ContentHandler):
    def __init__(self):
        # super(DBLPHandler, self).__init__()
        xml.sax.ContentHandler.__init__(self)
        self.PUB_TYPES = ["article", "inproceedings", "proceedings", "book", "incollection", "phdthesis", "mastersthesis", "www"]
        self.FIELDS = ["author", "editor", "title", "booktitle", "pages", "year", "address", "journal", "volume", "number", "month", "url", "ee", "cdrom", "cite", "publisher", "note", "crossref", "isbn", "series", "school", "chapter"]

        self.publication = None
        self.content = ''
        self.db = DB()

    def startElement(self, name, attrs):
        if name in self.PUB_TYPES:
            key = attrs.getValue("key")
            self.publication = Publication(name, key)
            self.content = ''

        if name in self.FIELDS:
            self.content = ''

    def endElement(self, name):
        if name in self.PUB_TYPES:
            self.db.dumps(self.publication)
        if name in self.FIELDS:
            self.publication.add_field(name, self.content)

    def characters(self, content):
        self.content += content.encode('utf-8').replace('\\','\\\\')


if __name__ == '__main__':
    dblp_fp = open('new.xml')
    handler = DBLPHandler()
    xml.sax.parse(dblp_fp, handler)
