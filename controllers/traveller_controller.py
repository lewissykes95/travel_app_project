from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.destination import Destination
from models.traveller import Traveller
import repositories.traveller_repository as traveller_repository
import repositories.destination_repository as destination_repository

travellers_blueprint = Blueprint("travellers", __name__)

@travellers_blueprint.route("/login")
def login():
    return render_template("login.html")

@travellers_blueprint.route("/about")
def about():
    return render_template("about.html")

#CREATE

@travellers_blueprint.route("/login", methods=['POST'])
def create_guest():
    name            = request.form['name']
    age             = request.form['age']
    traveller       = Traveller (name, age)
    traveller       = traveller_repository.save(traveller)
    return redirect('/login')

#DELETE

# @travellers_blueprint.route("/travellers/<id>/delete", methods=['POST'])
# def delete_traveller(id):
#     traveller_repository.delete(id)
#     return redirect ('/destinations/new')







