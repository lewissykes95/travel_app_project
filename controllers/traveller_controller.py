from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.traveller import Traveller
import repositories.traveller_repository as traveller_repository
import repositories.destination_repository as destination_repository

travellers_blueprint = Blueprint("travellers", __name__)

@travellers_blueprint.route("/travellers")
def travellers():
    return render_template("travellers/index.html")