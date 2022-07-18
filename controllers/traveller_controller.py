from flask import Flask, render_template, request, redirect
from flask import Blueprint
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

# @travellers_blueprint.route("/bucket-list", methods=['GET'])
# def list():
#     travellers = traveller_repository.select_all()
#     return render_template("travellers/bucket-list.html", travellers=travellers)



