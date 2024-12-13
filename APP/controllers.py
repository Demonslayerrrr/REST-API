import json
import os

class UserController:
    @staticmethod
    def read_users(id:int=None,file_name:str="users.json") -> str:
        try:
            file_path = os.path.join(os.path.dirname(__file__), f"../{file_name}")
            with open(file_path, "r") as f:
                users = json.load(f) 

                if id is not None:
                    users = users[id]
                return users
            
        except FileNotFoundError:
            raise ValueError("Users database not found")

    @staticmethod
    def add_users(new_user:json,file_name:str="users.json"):
        try:
            file_path = os.path.join(os.path.dirname(__file__), f"../{file_name}")
            with open(file_path, 'r') as file:
                users = json.load(file) 
        except FileNotFoundError:
            users = []

        users.append(new_user)

        with open(file_path, 'w') as file:
            json.dump(users, file, indent=4)

    @staticmethod
    def modify_users(user_info:json, id:int,file_name:str="users.json"):
        try:
            file_path = os.path.join(os.path.dirname(__file__), f"../{file_name}")
            with open(file_path, 'r') as file:
                users: list[dict] = json.load(file)

            for i, user in enumerate(users):
                if user.get("id") == id:
                    if "name" in user_info:
                        users[i]["name"] = user_info["name"]
                    if "last_name" in user_info:
                        users[i]["last_name"] = user_info["last_name"]
                    break
            
            with open(file_path, 'w') as file:
                json.dump(users, file, indent=4)

        except FileNotFoundError:
            raise ValueError("Users database not found")
        except Exception as e:
            raise e
        
    @staticmethod
    def replace_user(new_user:json,id:int,file_name:str="users.json"):
        try:
            file_path = os.path.join(os.path.dirname(__file__), f"../{file_name}")
            with open(file_path, 'r') as file:
                users: list[dict] = json.load(file)
            for i, user in enumerate(users):
                if user.get("id") == id:
                    users[i]["name"] = new_user["name"]
                    users[i]["last_name"] = new_user["last_name"]
                    break
            else:
                return None 
            
            with open(file_path, 'w') as file:
                json.dump(users, file, indent=4)
        except FileNotFoundError:
            raise ValueError("Users database not found")
        except Exception as e:
            raise e
        
    @staticmethod
    def delete_user(id:int,file_name:str="users.json"):
        try:
            file_path = os.path.join(os.path.dirname(__file__), f"../{file_name}")
            with open(file_path, 'r') as file:
                users: list[dict] = json.load(file)
            
            for i,user in enumerate(users):
                if user.get("id") == id:
                    del users[i]
            with open("../users.json", 'w') as file:
                json.dump(users, file, indent=4)
        except FileNotFoundError:
            raise ValueError("Users database not found")
        except Exception as e:
            raise e



            

            