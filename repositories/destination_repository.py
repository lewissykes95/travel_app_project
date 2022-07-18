from db.run_sql import run_sql
from models.destination import Destination
from models.traveller import Traveller


def save(destination):
    sql = "INSERT INTO destinations(city, country, continent) VALUES ( %s, %s, %s ) RETURNING id" 
    values = [destination.city, destination.country, destination.continent]
    results = run_sql( sql, values )
    destination.id = results[0]['id']
    return destination


def select_all():
    destinations = []

    sql = "SELECT * FROM destinations"
    results = run_sql(sql)

    for row in results:
        destination = Destination(row['city'], row['country'], row['continent'], row['id'])
        destinations.append(destination)
    return destination

def select(id):
    destination = None
    sql = "SELECT * FROM destinations WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        destination = Destination(result['city'], result['country'], result['continent'], result['id'])
    return 
    

def delete_all():
    sql = "DELETE FROM destinations"
    run_sql(sql)