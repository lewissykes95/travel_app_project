# from db.run_sql import run_sql
# from models.visit import Visit
# from models.traveller import Traveller
# import repositories.traveller_repository as traveller_repository
# from models.destination import Destination
# import repositories.destination_repository as destination_repository

# def save(visit):
#     sql = "INSERT INTO visits (traveller_id, destination_id VALUES (%s, %s) RETURNING id"
#     values = [visit.traveller.id, visit.destination.id]
#     results = run_sql(sql, values)
#     id = results[0]['id']
#     visit.id = id  

# def select_all():
#     visits = []
#     sql = "SELECT * FROM visits"
#     results = run_sql(sql)
#     for result in results:
#         traveller = traveller_repository.select(result["traveller_id"])
#         destination = destination_repository.select(result["destination_id"])
#         visit = Visit(traveller, destination, result["id"])
#         visits.append(visit)
#     return visits 

# def select(id):
#     visit = None
#     sql = "SELECT * FROM visits WHERE id = %s"
#     values = [id]

#     results = run_sql(sql, values)

#     if results:
#         result = results[0]
#         traveller = traveller_repository.select(result['traveller_id'])
#         destination = destination_repository.select(result["destination_id"])
#         visit - Visit(traveller, destination, result["id"])
#     return visit


# def delete_all():
#     sql = "DELETE FROM visits"
#     run_sql(sql)

# def delete(id):
#     sql = "DELETE FROM visits WHERE id = %s"
#     values = [id]
#     run_sql(sql)

# def update(visit):
#     sql = "UPDATE visits SET (traveller_id, destination_id) = (%s, %s) WHERE id = %s"
#     values = [visit.traveller.id, visit.destination.id, visit.id]
#     run_sql(sql, values)

