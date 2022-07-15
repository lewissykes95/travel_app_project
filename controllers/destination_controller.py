from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.destination import Destination
import repositories.traveller_repository as traveller_repoository
import repositories.destination_repository as destination_repository

