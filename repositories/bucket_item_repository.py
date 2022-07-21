from db.run_sql import run_sql
from models.bucket_item import BucketItem
from models.destination import Destination
from models.traveller import Traveller
from models.country import Country

def save(bucket_item):
    sql = "INSERT INTO countries( name, traveller_id, destination_id, visited) VALUES ( %s ) RETURNING id"
    values = [bucket_item.name]
    results = run_sql( sql, values )
    bucket_item.id = results[0]['id']
    return bucket_item

def select_all():
    bucket_list = []

    sql = "SELECT * FROM countries"
    results = run_sql(sql)
    for row in results:
        bucket_item = BucketItem(row['name'], row['id'])
        bucket_list.append(bucket_item)
    return bucket_list










