from flask import Flask, request, jsonify 
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
from flask_restful import Resource, Api
from dotenv import load_dotenv
import os

load_dotenv()


app = Flask(__name__) 
api = Api(app) 
URL = os.getenv("URL")
app.config['SQLALCHEMY_DATABASE_URI'] = URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app) 
ma = Marshmallow(app)
 
class Computer(db.Model):

    computer_id = db.Column(db.BigInteger , nullable = False, unique = True, primary_key = True)
    harddrive_type = db.Column(db.String(55), nullable = False)
    processor = db.Column(db.String(55), nullable=False)
    ram_amount = db.Column(db.String(55), nullable = False)
    max_ram = db.Column(db.String(55) , nullable = False)
    harddrive_space = db.Column(db.String(55), nullable = False)
    form_factor = db.Column(db.String(55))

    def __init__(self, harddrive_type, processor, ram_amount, max_ram, harddrive_space, form_factor):

        self.harddrive_type = harddrive_type
        self.processor = processor
        self.ram_amount = ram_amount
        self.max_ram = max_ram
        self.harddrive_space = harddrive_space
        self.form_factor = form_factor

class ComputerSchema(ma.Schema):
    class Meta:
        fields = ('computer_id', 'harddrive_type', 'processor', 'ram_amount', 'max_ram', 'harddrive_space', 'form_factor')

db.create_all()

class ComputerManager(Resource):
    
    @staticmethod
    def get():
        computers_schema = ComputerSchema(many=True)
        computers = Computer.query.all()
        return jsonify(computers_schema.dump(computers))
        
    @staticmethod
    def post():
        harddrive_type= request.json['harddrive_type']
        processor = request.json['processor']
        ram_amount = request.json['ram_amount']
        max_ram = request.json['max_ram']
        harddrive_space = request.json['harddrive_space']
        form_factor = request.json['form_factor']

        computer = Computer(harddrive_type, processor, ram_amount, max_ram, harddrive_space, form_factor)
        db.session.add(computer)
        db.session.commit()

        return jsonify({
            'Message': f'Computer inserted.'
        })

    @staticmethod
    def put():
        try: id = request.args['computer_id']
        except Exception as _: id = None

        if not id:
            return jsonify({ 'Message': 'Must provide the computer ID' })

        computer = Computer.query.get(id)
        harddrive_type= request.json['harddrive_type']
        processor = request.json['processor']
        ram_amount = request.json['ram_amount']
        max_ram = request.json['max_ram']
        harddrive_space = request.json['harddrive_space']
        form_factor = request.json['form_factor']

        computer.harddrive_type = harddrive_type
        computer.processor = processor
        computer.ram_amount = ram_amount
        computer.max_ram = max_ram
        computer.harddrive_space = harddrive_space
        computer.form_factor = form_factor

        db.session.commit()
        return jsonify({
            'Message': f'Computer {id} changed.'
        })

    @staticmethod
    def delete():
        try: id = request.args['computer_id']
        except Exception as _: id = None

        if not id:
            return jsonify({ 'Message': 'Must provide the computer ID' })

        computer = Computer.query.get(id)
        db.session.delete(computer)
        db.session.commit()

        return jsonify({
            'Message': f'Computer {id} deleted.'
        })


if __name__ == '__main__':
    api.add_resource(ComputerManager, '/api/computers')
    app.run(debug=True)