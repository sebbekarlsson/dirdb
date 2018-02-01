import os
import json
from graphql.parser import GraphQLParser


class QueryHandler(object):

    def __init__(self):
        pass

    def execute(self, query):
        print(query)
        parser = GraphQLParser()

        try:
            parsed = parser.parse(query)
        except Exception:
            return json.dumps({'error': 'parse error'})

        return json.dumps({'data': str(parsed)})

    def db_exists(self, db):
        return os.path.isdir(os.path.join(self.base_dir, db))

    def create_db(self, db):
        return os.mkdir(os.path.join(self.base_dir, db))

    def save_document(self, db, name, document):
        if not self.db_exists(db):
            self.create_db(db)

        filepath = os.path.join(self.base_dir, db, name + '.json')

        if not os.path.isfile(filepath):
            with open(filepath, 'w+') as _file:
                _file.write('')
            _file.close()

        filecontents = ''
        with open(filepath) as _file:
            filecontents = _file.read()
        _file.close()

        filecontents = '[]' if not filecontents else filecontents

        data = json.loads(filecontents)

        data.append(document)

        with open(filepath, 'w+') as _file:
            _file.write(json.dumps(data))
        _file.close()

    def update_document(self, db, query, document):
        current = self.find_document(query)
        print(current)

    def delete_document(self, db, query):
        current = self.find_document(query)
        print(current)

    def find_document(self, db, query):
        filepath = os.path.join(self.base_dir, db, query['$name'] + '.json')

        contents = ''
        with open(filepath, 'r+') as _file:
            contents = _file.read()
        _file.close()
        contents = '[]' if not contents else contents

        return json.loads(contents)
