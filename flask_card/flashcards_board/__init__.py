from flask import Blueprint

flashcards_board = Blueprint("flashcards_board", __name__)

from . import views
