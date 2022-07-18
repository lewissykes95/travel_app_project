from db.run_sql import run_sql
from models.destination import Destination
from models.traveller import Traveller


def save(traveller):
    sql = "INSERT INTO travellers( name, age ) VALUES ( %s, %s ) RETURNING id"
    values = [traveller.name, traveller.age]
    results = run_sql( sql, values )
    traveller.id = results[0]['id']
    return traveller

def select_all():
    travellers = []

    sql = "SELECT * FROM travellers"
    results = run_sql(sql)
    for row in results:
        traveller = Traveller(row['name'], row['age'], row['id'])
        travellers.append(traveller)
    return travellers

def select(id):
    traveller = None
    sql = "SELECT * FROM travellers WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results: 
        result = results[0]
        traveller = Traveller(result['name'], result['age'], result['id'])
    return traveller


def delete_all():
    sql = "DELETE FROM travellers"
    run_sql(sql)





