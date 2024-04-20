import mysql.connector

#configurar conex
mysql_config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'paginaBD',
    'auth_plugin': 'mysql_native_password'
}

connection = mysql.connector.connect(**mysql_config)

def get_connection():
    return connection