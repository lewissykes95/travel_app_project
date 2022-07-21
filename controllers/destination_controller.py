from crypt import methods
from types import CoroutineType
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.destination import Destination
import repositories.traveller_repository as traveller_repository
import repositories.destination_repository as destination_repository

destinations_blueprint = Blueprint("destinations", __name__)

# INDEX 

@destinations_blueprint.route("/destinations/new")
def destination_new():
    #GET the destinations from the DB
    destinations = destination_repository.select_all()
    travellers = traveller_repository.select_all()
    # Pass the destinations to the template 
    return render_template("destinations/new.html", all_destinations=destinations, all_travellers=travellers) 


@destinations_blueprint.route("/Voyager")
def home():
    return render_template("index.html")

# NEW
# GET 

# CREATE

@destinations_blueprint.route("/destinations/new", methods=['POST'])
def create_destination():
    traveller_id    = request.form['traveller_id']
    city            = request.form['city']
    country         = request.form['country']
    duration        = request.form['duration']
    checked_off     = request.form['done']
    traveller       = traveller_repository.select(traveller_id)
    destination     = Destination (traveller, city, country, duration, checked_off)
    destination_repository.save(destination)
    return redirect('/destinations/new')


@destinations_blueprint.route("/bucket-list", methods=['GET'])
def show_bucket_list():
    destinations = destination_repository.select_all()
    travellers = traveller_repository.select_all()
    return render_template('destinations/index.html', all_destinations = destinations, all_travellers = travellers)


# SHOW

@destinations_blueprint.route("/destinations/<id>", methods=['GET'])
def show_destination(id):
    destination = destination_repository.select(id)
    traveller= traveller_repository.select(id)
    return render_template('destinations/show.html', destination = destination, traveller = traveller) 

#EDIT

@destinations_blueprint.route("/destinations/<id>/edit", methods=['GET'])
def edit_destination(id):
    destination = destination_repository.select(id)
    travellers = traveller_repository.select_all()
    return render_template('destinations/edit.html', destination = destination, all_travellers = travellers)

#UPDATE

@destinations_blueprint.route("/destinations/<id>", methods=["Post"])
def update_destination(id):
    traveller_id    = request.form['traveller_id']
    city            = request.form['city']
    country         = request.form['country']
    duration        = request.form['duration']
    checked_off     = request.form['done']
    traveller       = traveller_repository.select(traveller_id)
    destination     = destination_repository.select(id)
    destination.traveller = traveller
    destination.city = city
    destination.country = country
    destination.duration = duration
    destination.checked_off = checked_off
    destination_repository.update(destination)
    return redirect('/bucket-list') 


# DELETE

@destinations_blueprint.route("/destinations/<id>/delete", methods=['POST'])
def delete_destination(id):
    destination_repository.delete(id)
    return redirect('/bucket-list')


@destinations_blueprint.route("/destinations/amsterdam")
def amsterdam():
    return render_template("destinations/amsterdam.html")



@destinations_blueprint.route("/destinations/sydney")
def sydney():
    return render_template("destinations/sydney.html")


@destinations_blueprint.route("/destinations/rio")
def rio():
    return render_template("destinations/rio.html")


@destinations_blueprint.route("/destinations/going/<id>", methods=['GET'])
def show_destination_going(id):
    destination = destination_repository.select(id)
    traveller = traveller_repository.select(id)
    return render_template('destinations/going.html', destination = destination, traveller = traveller) 













   
    





