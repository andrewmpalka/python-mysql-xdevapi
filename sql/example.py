import mysqlx

# Connect to server on localhost
session = mysqlx.get_session({
    'host': 'localhost',
    'port': 33060,
    'user': 'root',
    'password': 'Password123!'
})

schema = session.get_schema('test')

# Use the collection 'my_collection'
collection = schema.get_collection('my_collection');

# Specify which document to find with Collection.find()
result = collection.find('name like :param').bind('param', 'S%').limit(1).execute()

docs = result.fetch_all()
print(f"Name: {docs[0].name}"

session.close()
