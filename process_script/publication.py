"""
Publication Object for dump data into MySQL
"""


class Publication(object):
    def __init__(self, pub_type, key):
        super(Publication, self).__init__() 
        self.pub_type = pub_type
        self.key = key
        self.fields = {
            "author" : [], 
            "editor" : [], 
            "title" : None, 
            "booktitle" : None, 
            "pages" : None, 
            "year" : None, 
            "address" : None, 
            "journal" : None, 
            "volume" : None, 
            "number" : None, 
            "month" : None, 
            "url" : None, 
            "ee" : None, 
            "cdrom" : None, 
            "cite" : None, 
            "publisher" : None, 
            "note" : None, 
            "crossref" : None, 
            "isbn" : None, 
            "series" : None, 
            "school" : None, 
            "chapter" : None,
        }

    def add_field(self, field, value):
        if field == 'author':
            self.fields['author'].append(value)
        elif field == 'editor':
            self.fields['editor'].append(value)
        elif field == 'year':
            self.fields['year'] = int(value)
        else:
            self.fields[field] = value

    def data_tuple(self):
        return (
                self.key, 
                self.pub_type, 
                # str(self.fields["author"]), 
                str(self.fields["editor"]),  
                self.fields["title"], 
                self.fields["booktitle"], 
                self.fields["pages"], 
                self.fields["year"], 
                self.fields["address"], 
                self.fields["journal"], 
                self.fields["volume"], 
                self.fields["number"], 
                self.fields["month"], 
                self.fields["url"], 
                self.fields["ee"], 
                self.fields["cdrom"], 
                self.fields["cite"], 
                self.fields["publisher"], 
                self.fields["note"], 
                self.fields["crossref"], 
                self.fields["isbn"], 
                self.fields["series"], 
                self.fields["school"], 
                self.fields["chapter"],
        )