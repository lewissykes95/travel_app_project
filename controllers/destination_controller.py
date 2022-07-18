from types import CoroutineType
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.destination import Destination
import repositories.traveller_repository as traveller_repository
import repositories.destination_repository as destination_repository

destinations_blueprint = Blueprint("destinations", __name__)

# INDEX 
@destinations_blueprint.route("/destinations")
def destinations():
    #GET the destinations from the DB
    destinations = destination_repository.select_all()
    travellers = traveller_repository.select_all()
    # Pass the destinations to the template 
    return render_template("destinations/new.html", all_destinations=destinations, all_travellers=travellers) 

# NEW
# GET '/tasks/new'
@destinations_blueprint.route("/destinations/new", methods=['GET'])
def new_destination():
    travellers = traveller_repository.select_all()
    return render_template("destinations/new.html", all_travellers=travellers)

# CREATE
# POST '/tasks'

@destinations_blueprint.route("/bucket-list", methods=['POST'])
def create_destination():
    traveller_id    = request.form['traveller_id']
    city            = request.form['city']
    country         = request.form['country']
    duration        = request.form['duration']
    checked_off     = request.form['done']
    traveller       = traveller_repository(traveller_id)
    destination     = Destination (traveller, city, country, duration, checked_off)
    destination_repository.save(destination)
    return redirect('/bucket-list') 

# SHOW
# GET '/tasks/<id>'
@tasks_blueprint.route("/destinations/<id>", methods=['GET'])
def show_destination(id):
    destination = destination_repository.select(id)
    return render_template('destination/show.html', destination = destination)


@destinations_blueprint.route("/destinations/amsterdam")
def amsterdam():
    return render_template("destinations/amsterdam.html")

@destinations_blueprint.route("/destinations/rio")
def rio():
    return render_template("destinations/rio.html")

@destinations_blueprint.route("/destinations/sydney")
def sydney():
    return render_template("destinations/sydney.html")

@destinations_blueprint.route("/bucket-list", methods=['GET'])
def list():
    destinations = destination_repository.select_all()
    return render_template("travellers/list.html", destination=destinations)






   
    





