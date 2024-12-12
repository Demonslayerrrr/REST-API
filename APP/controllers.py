import json

class UserController:
    @staticmethod
    def read_users(id:int=None) -> str:
        try:
            with open("users.json", "r") as f:
                users = json.load(f) 

                if id is not None:
                    users = users[id]
                return users
            
        except FileNotFoundError:
            raise ValueError("Users database not found")

    @staticmethod
    def add_users(new_user:json):
        try:
            with open("users.json", 'r') as file:
                users = json.load(file) 
        except FileNotFoundError:
            users = []

        users.append(new_user)

        with open("users.json", 'w') as file:
            json.dump(users, file, indent=4)

    @staticmethod
    def modify_users(user_info:json, id:int):
        try:
            with open("users.json", 'r') as file:
                users: list[dict] = json.load(file)

            for i, user in enumerate(users):
                if user.get("id") == id:
                    if "name" in user_info:
                        users[i]["name"] = user_info["name"]
                    if "last_name" in user_info:
                        users[i]["last_name"] = user_info["last_name"]
                    break
            
            with open("users.json", 'w') as file:
                json.dump(users, file, indent=4)

        except FileNotFoundError:
            raise ValueError("Users database not found")
        except Exception as e:
            raise e
        
    @staticmethod
    def replace_user(new_user:json,id:int):
        try:
            with open("users.json", 'r') as file:
                users: list[dict] = json.load(file)
            for i, user in enumerate(users):
                if user.get("id") == id:
                    users[i]["name"] = new_user["name"]
                    users[i]["last_name"] = new_user["last_name"]
                    break
            else:
                return None 
            
            with open("users.json", 'w') as file:
                json.dump(users, file, indent=4)
        except FileNotFoundError:
            raise ValueError("Users database not found")
        except Exception as e:
            raise e
        
    @staticmethod
    def delete_user(id:int):
        try:
            with open("users.json", 'r') as file:
                users: list[dict] = json.load(file)
            
            for i,user in enumerate(users):
                if user.get("id") == id:
                    del users[i]
            with open("users.json", 'w') as file:
                json.dump(users, file, indent=4)
        except FileNotFoundError:
            raise ValueError("Users database not found")
        except Exception as e:
            raise e



            

            