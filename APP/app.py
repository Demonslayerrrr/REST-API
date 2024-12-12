from flask import Flask,jsonify,request
from flask.typing import ResponseReturnValue
from controllers import UserController
from json import dump, load

app = Flask(__name__)


@app.get("/users")
def print_users():
    controller = UserController()
    body = controller.read_users()
    return jsonify(body),200

@app.get("/users/<int:user_id>")
def print_user_with_id(user_id):
    controller = UserController()
    body = controller.read_users(user_id)
    return jsonify(body),200



@app.post("/users")
def post_user():
    new_user_data = request.get_json()

    name,last_name = new_user_data["name"], new_user_data["last_name"]

    controller = UserController()

    users = controller.read_users()

    current_id = len(users)

    new_user = {
        "id": current_id+1,
        "name": name,
        "last_name":last_name
    }

    controller.add_users(new_user)

    return jsonify(controller.read_users()),201

@app.patch("/users/<int:id>")
def patch_user(id:int):
    controller = UserController()

    try:
        new_user_data = request.get_json()


        name = new_user_data.get("name")
        last_name = new_user_data.get("last_name")
        
        new_user = {}
        if name:
            new_user["name"] = name
        if last_name:
            new_user["last_name"] = last_name

        controller.modify_users(new_user, id)


        return '', 204  

    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@app.put("/users/<int:id>")
def put_user(id:int):

    controller = UserController()

    try:
        new_user_data = request.get_json()


        name = new_user_data.get("name")
        last_name = new_user_data.get("last_name")

        new_user = {
            "id":id,
            "name":name,
            "last_name":last_name
        }

        controller.replace_user(new_user, id)

        return '', 204  

    
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@app.delete("/users/<int:id>")
def remove_user(id:int):
    controller = UserController()

    try:
        controller.delete_user(id)
        return '',204

    except Exception as e:
        return jsonify({"error":str(e)}),400



if __name__ == "__main__":
    app.run(debug=True) 