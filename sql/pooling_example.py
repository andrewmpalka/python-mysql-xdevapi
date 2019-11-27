import mysqlx

connection_str = 'mysqlx://root:oYIrkcXq4D@127.0.0.1:33060'
connection_dict = {
    'host': '127.0.0.1',
    'port': 33060,
    'user': 'root',
    'password': 'oYIrkcXq4D'
}

client = mysqlx.get_client(connection_dict, {'pooling':{'max_size': 5, 'queue_timeout': 1000}})
session = client.get_session()

# (...)

client.close()
