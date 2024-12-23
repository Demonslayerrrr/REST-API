from APP import app,controllers
import json
import os


def test_print_users():
    with app.app.test_request_context():
        users = b'[{"id":1,"last_name":"Oczkowski","name":"Wojciech"},{"id":2,"last_name":"Naishtetik","name":"Ilia"},{"id":3,"last_name":"Pork","name":"Jon"}]\n'
        response,status_code = app.print_users()

        assert users == response.data
        
def test_print_users_with_id():
    with app.app.test_request_context():
        user = b'{"id":1,"last_name":"Oczkowski","name":"Wojciech"}\n'
        id = 0
        response,status_code = app.print_user_with_id(id)

        assert response.data == user

def test_post_users():
    with app.app.test_request_context():
        user = {"id":1,"name":"a","last_name":"b"}
        controller = controllers.UserController()

        controller.add_users(user,"test_database.json")

        file_path = os.path.join(os.path.dirname(__file__), f"../test_database.json")
        with open(file_path, 'r') as file:
            users: list[dict] = json.load(file)
        assert user in users

        users = [u for u in users if u.get("id") != user.get("id")]


        with open(file_path, 'w') as file:
            json.dump(users, file)


        with open(file_path, 'r') as file:
            updated_users = json.load(file)
        assert user not in updated_users


def test_patch_user():
    with app.app.test_request_context():
        controller = controllers.UserController()
        
     
        user = {"id": 2, "name": "a", "last_name": "b"}

        controller.add_users(user, "test_database.json")

        file_path = os.path.join(os.path.dirname(__file__), f"../test_database.json")
        

        with open(file_path, 'r') as file:
            users: list[dict] = json.load(file)


        controller.modify_users({"name": "S"}, 2, "test_database.json")

        with open(file_path, 'r') as file:
            updated_users: list[dict] = json.load(file)


        assert {"id": 2, "name": "S", "last_name": "b"} in updated_users

        updated_users = [u for u in updated_users if u.get("id") != user.get("id")]

        with open(file_path, 'w') as file:
            json.dump(updated_users, file)


def test_put_user():
        with app.app.test_request_context():
            controller = controllers.UserController()
            
        
            user = {"id": 2, "name": "a", "last_name": "b"}

            controller.add_users(user, "test_database.json")

            file_path = os.path.join(os.path.dirname(__file__), f"../test_database.json")
            

            with open(file_path, 'r') as file:
                users: list[dict] = json.load(file)


            controller.modify_users({"name": "S"}, 2, "test_database.json")

            with open(file_path, 'r') as file:
                updated_users: list[dict] = json.load(file)


            assert {"id": 2, "name": "S", "last_name": "b"} in updated_users

            updated_users = [u for u in updated_users if u.get("id") != user.get("id")]

            with open(file_path, 'w') as file:
                json.dump(updated_users, file)

def test_remove_user():
    with app.app.test_request_context():
        controller = controllers.UserController()


        user = {"id": 2, "name": "a", "last_name": "b"}
        controller.add_users(user, "test_database.json")

        file_path = os.path.join(os.path.dirname(__file__), "../test_database.json")
        with open(file_path, 'r') as file:
            users: list[dict] = json.load(file)
        assert user in users

        controller.delete_user(2, "test_database.json")

        with open(file_path, 'r') as file:
            updated_users: list[dict] = json.load(file)

        assert user not in updated_users


