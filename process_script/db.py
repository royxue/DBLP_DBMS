"""
Database Object
"""
import MySQLdb


class DB(object):
    def __init__(self):
        super(DB, self).__init__()
        self.conn = MySQLdb.connect('localhost', 'root', '', 'soc2')
        self.cursor = self.conn.cursor(MySQLdb.cursors.DictCursor)

    def dumps(self, record):
        # insert into paper table
        query = """
            INSERT INTO publications (pub_key, pub_type, editor, title, booktitle, pages, pub_year, address, journal, volume, number, pub_month, url, ee, cdrom, cite, publisher, note, crossref, isbn, series, school, chapter)
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        self.cursor.execute(query, record.data_tuple())
        pub_id = self.cursor.lastrowid
        self.conn.commit()

        # handle authors
        authors = record.fields['author']
        for author in authors:
            query = """
                INSERT INTO authors (author)
                VALUES(%s)
                ON DUPLICATE KEY UPDATE id=LAST_INSERT_ID(id)
            """
            self.cursor.execute(query, (author))
            author_id = self.conn.insert_id()
            self.conn.commit()

            # insert many-to-many relationship
            query = """
                INSERT INTO authors_publications(author_id, publication_id)
                VALUES(%s, %s)
            """
            try:
                self.cursor.execute(query, (author_id, pub_id))
                self.conn.commit()
            except:
                pass

    def close(self):
        self.conn.close()
