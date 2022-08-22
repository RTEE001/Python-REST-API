from flask import request, jsonify
from umuzi_computers import ComputerSchema, Computer, db, app
from enum import Enum

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
    return FormFactor.has_value(form_factor)

def check_harddrive_type(harddrive_type):
    return HardDriveType.has_value(harddrive_type)
         

def form_factor_messages():
    return jsonify({"Message": 'Form factor should be either mini, mini-atx or  micro'})

def harddrive_type_messages():
    return jsonify({"Message": 'Hard drive type should be either ssd or hdd'})

@app.route("/computers", methods=["POST"])
def post():
    
    form_factor = request.json["form_factor"]
    harddrive_type = request.json["harddrive_type"]

    if not check_form_factor(form_factor):
        form_factor_messages()
    if not check_harddrive_type(harddrive_type):
        harddrive_type_messages()

    processor = request.json["processor"]
    ram_amount = request.json["ram_amount"]
    max_ram = request.json["max_ram"]
    harddrive_space = request.json["harddrive_space"]
    

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
            if not check_harddrive_type(harddrive_type):
                harddrive_type_messages()
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
            if not check_form_factor(form_factor):
                form_factor_messages()   
            computer.form_factor = form_factor     
    

    db.session.commit()
    return jsonify({"Message": f"Computer {id} altered."})
        

if __name__ == "__main__":
    app.run(debug=True)
