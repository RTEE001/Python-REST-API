from flask import request, jsonify
from umuzi_computers import ComputerSchema, Computer, db, app
from enum import Enum
from werkzeug.exceptions import BadRequest


class FormFactor(Enum):
    MINI = 'mini'
    MINI_ATX = 'mini-atx'
    MICRO = 'micro'

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_

class HardDriveType(Enum):
    SSD = 'ssd'
    HDD = 'hdd'

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_

def check_form_factor(form_factor):
    if not FormFactor.has_value(form_factor):
        raise BadRequest('Form factor should be either mini, mini-atx or  micro')
    return True

def check_harddrive_type(harddrive_type):
    if not HardDriveType.has_value(harddrive_type):
        raise BadRequest('Hard drive type should be either ssd or hdd')
    return True

@app.route("/computers", methods=["POST"])
def post():
    
    form_factor = request.json["form_factor"]
    harddrive_type = request.json["harddrive_type"]
    processor = request.json["processor"]
    ram_amount = request.json["ram_amount"]
    max_ram = request.json["max_ram"]
    harddrive_space = request.json["harddrive_space"]

    check_form_factor(form_factor)
    check_harddrive_type(harddrive_type)

    new_computer = Computer(
        harddrive_type, processor, ram_amount, max_ram, harddrive_space, form_factor
    )
    db.session.add(new_computer)
    db.session.commit()

    return jsonify({"Message": "Computer inserted."})



@app.route("/computers", methods=["GET"])
def get():

    computers_schema = ComputerSchema(many=True)
    computers = Computer.query.all()
    return jsonify(computers_schema.dump(computers))


@app.route("/computers/<id>", methods=["DELETE"])
def delete(id):

    computer = Computer.query.get(id)
    db.session.delete(computer)
    db.session.commit()

    return jsonify({"Message": f"Computer {id} deleted."})


@app.route("/computers/<id>", methods=['PUT'])
def put(id):

    computer = Computer.query.get(id)

    if "harddrive_type" in request.json:
        harddrive_type = request.json["harddrive_type"]
        check_harddrive_type(harddrive_type)
        computer.harddrive_type = harddrive_type

    if "processor" in request.json:
        processor = request.json["processor"]
        computer.processor = processor

    if "ram_amount" in request.json:
        ram_amount = request.json["ram_amount"]
        computer.ram_amount = ram_amount
    

    if "max_ram" in request.json:
        max_ram = request.json["max_ram"]
        computer.max_ram = max_ram

    if "harddrive_space" in request.json:
        harddrive_space = request.json["harddrive_space"]
        computer.harddrive_space = harddrive_space 

    if "form_factor" in request.json:
        form_factor = request.json["form_factor"]
        check_form_factor(form_factor)  
        computer.form_factor = form_factor 

    db.session.commit()
    return jsonify({"Message": f"Computer {id} altered."})
        

if __name__ == "__main__":
    app.run(debug=False)
