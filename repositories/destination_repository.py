from db.run_sql import run_sql
from models.destination import Destination
from models.traveller import Traveller
import repositories.traveller_repository as traveller_repository

def save(destination):
    sql = "INSERT INTO destinations(traveller_id, city, country, duration, checked_off ) VALUES ( %s, %s, %s, %s, %s ) RETURNING id" 
    values = [destination.traveller.id, destination.city, destination.country, destination.duration, destination.checked_off]
    results = run_sql( sql, values )
    destination.id = results[0]['id']
    return destination



def select_all():
    destinations = []

    sql = "SELECT * FROM destinations"
    results = run_sql(sql)

    for row in results:
        traveller = traveller_repository.select(row['traveller_id'])
        destination = Destination(traveller, row['city'], row['country'], row['duration'], row['checked_off'], row['id'])
        destinations.append(destination)
    return destination

def select(id):
    destination = None
    sql = "SELECT * FROM destinations WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results is not None:
        result = results[0]
        traveller = traveller_repository.select(result['traveller_id'])
        destination = Destination(traveller, result['city'], result['country'], result['duration'], result['checked_off'], result['id'])
    return destination
    

def delete_all():
    sql = "DELETE FROM destinations"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM destinations WHERE id = %s"
    values = [id]
    run_sql(sql, values)



def update(destination):
    sql = "UPDATE destinations SET (traveller_id, city, country, duration, checked_off) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [destination.traveller.id, destination.city, destination.country, destination.duration, destination.checked_off, destination.id]
    run_sql(sql, values)

