from flask import request, jsonify
from umuzi_computers import ComputerSchema, Computer, db, app
from flask_restful import Resource
from enum import Enum

class FormFactor(Enum):
    MINI = 'mini'
    MINI_ATX = 'mini-atx'
    MICRO = 'mini-micro-atx'

class HardDriveType(Enum):
    SSD = 'ssd'
    HDD = 'hdd'


@app.route("/computers", methods=["POST"])
def post():
    
    harddrive_type = request.json["harddrive_type"]
    processor = request.json["processor"]
    ram_amount = request.json["ram_amount"]
    max_ram = request.json["max_ram"]
    harddrive_space = request.json["harddrive_space"]
    form_factor = request.json["form_factor"]

    new_computer = Computer(
        harddrive_type, processor, ram_amount, max_ram, harddrive_space, form_factor
    )
    db.session.add(new_computer)
    db.session.commit()

    return jsonify({"Message": f"Computer inserted."})



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

    for element in request.json:

        if element=="harddrive_type":
            harddrive_type = request.json["harddrive_type"]
            computer.harddrive_type = harddrive_type

        elif element=="processor":
            processor = request.json["processor"]
            computer.processor = processor

        elif element=="ram_amount":
            ram_amount = request.json["ram_amount"]
            computer.ram_amount = ram_amount

        elif element=="max_ram":
            max_ram = request.json["max_ram"]
            computer.max_ram = max_ram

        elif element=="harddrive_space":
            harddrive_space = request.json["harddrive_space"]
            computer.harddrive_space = harddrive_space  

        elif element=="form_factor":
            form_factor = request.json["form_factor"]
            computer.form_factor = form_factor     
    

    db.session.commit()
    return jsonify({"Message": f"Computer {id} altered."})
        

if __name__ == "__main__":
    app.run(debug=False)
