from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api
from dotenv import load_dotenv
import os


load_dotenv()
app = Flask(__name__)
api = Api(app)
SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Computer(db.Model):

    id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True)
    harddrive_type = db.Column(db.String(55), nullable=False)
    processor = db.Column(db.String(55), nullable=False)
    ram_amount = db.Column(db.Numeric, nullable=False)
    max_ram = db.Column(db.Numeric, nullable=False)
    harddrive_space = db.Column(db.Numeric, nullable=False)
    form_factor = db.Column(db.String(55))

    def __init__(
        self,
        harddrive_type,
        processor,
        ram_amount,
        max_ram,
        harddrive_space,
        form_factor,
    ):

        self.harddrive_type = harddrive_type
        self.processor = processor
        self.ram_amount = ram_amount
        self.max_ram = max_ram
        self.harddrive_space = harddrive_space
        self.form_factor = form_factor


class ComputerSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "harddrive_type",
            "processor",
            "ram_amount",
            "max_ram",
            "harddrive_space",
            "form_factor",
        )
        model = Computer


db.create_all()
