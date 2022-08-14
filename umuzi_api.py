from flask import request, jsonify 
from flask_restful import Resource
from umuzi_computers import Computer,ComputerSchema,db,app

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

#     api.add_resource(UserManager, '/api/users')

# if __name__ == '__main__':
#     app.run(debug=True)