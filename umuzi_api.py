from flask import request, jsonify
from umuzi_computers import ComputerSchema, Computer, db, app
from flask_restful import Resource


class ComputerManager(Resource):
    @staticmethod
    @app.route("/computers", methods=["GET"])
    def get():

        computers_schema = ComputerSchema(many=True)
        computers = Computer.query.all()
        return jsonify(computers_schema.dump(computers))

    @staticmethod
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

    @staticmethod
    @app.route("/edit-computer", methods=["PUT"])
    def put():
        try:
            id = request.args["id"]
        except Exception as _:
            id = None

        if not id:
            return jsonify({"Message": "Must provide the computer ID"})

        computer = Computer.query.get(id)
        harddrive_type = request.json["harddrive_type"]
        processor = request.json["processor"]
        ram_amount = request.json["ram_amount"]
        max_ram = request.json["max_ram"]
        harddrive_space = request.json["harddrive_space"]
        form_factor = request.json["form_factor"]

        computer.harddrive_type = harddrive_type
        computer.processor = processor
        computer.ram_amount = ram_amount
        computer.max_ram = max_ram
        computer.harddrive_space = harddrive_space
        computer.form_factor = form_factor

        db.session.commit()
        return jsonify({"Message": f"Computer {id} altered."})

    @staticmethod
    @app.route("/delete-computer", methods=["DELETE"])
    def delete():
        try:
            id = request.args["id"]
        except Exception as _:
            id = None

        if not id:
            return jsonify({"Message": "Must provide the computer ID"})

        computer = Computer.query.get(id)
        db.session.delete(computer)
        db.session.commit()

        return jsonify({"Message": f"Computer {id} deleted."})


if __name__ == "__main__":
    app.run(debug=False)
