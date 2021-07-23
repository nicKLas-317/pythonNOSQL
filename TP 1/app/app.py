from flask import Flask
from sqlalchemy import create_engine, MetaData, Table, Column, Float, Integer, String, ForeignKey
from sqlalchemy.ext.automap import automap_base

app = Flask(__name__)

# DB Config
confDB = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'classicmodels'
    }

db_user = confDB.get('user')
db_pwd = confDB.get('password')
db_host = confDB.get('host')
db_port = confDB.get('port')
db_name = confDB.get('database')

connection_str = f'mysql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}'
engine = create_engine(connection_str)
connection = engine.connect()

if connection:
        print(' Connection à Docker container via Python success ;)')
else:
        print('Connexion échouée :(')


# Get (or pull) MetaDatas
datas = MetaData(bind=engine)
datas.reflect(only=['customers','employees','offices', 'orderdetails','orders','payments','productlines','products'])

#mapping metadatas
db = automap_base(metadata=datas)
db.prepare()
payments = db.classes.payments

if __name__ == '__main__':
    app.run(debug=True)