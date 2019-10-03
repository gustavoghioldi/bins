from flask import Flask, request
import peewee
from playhouse.shortcuts import model_to_dict

app = Flask(__name__)
mysql_db = peewee.MySQLDatabase('bins', user='root', password='root',
                         host='127.0.0.1', port=3306)

class Discovery(peewee.Model):
    id = peewee.IntegerField()
    brand = peewee.CharField()
    category=peewee.CharField()
    issuer = peewee.CharField()
    bank = peewee.CharField()
    country = peewee.CharField()

    class Meta:
        database=mysql_db
        db_table='binTable'

@app.route('/<int:bin>')
def respon(bin):
    a = Discovery.select().where(Discovery.id == bin).get()
    return model_to_dict(a)