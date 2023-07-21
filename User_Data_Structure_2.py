#Create a DS containing 100 miliion record and perform insertion, search, update and list operation effeciently.

from typing import Any


class user:
    def __init__(self,username,name,email):
        self.username = username
        self.name = name
        self.email = email
    #     print('User created : <<{}>>'.format(self.username))

    def __repr__(self):
        return "USERNAME: {}    NAME: {}    EMAIL: {}".format(self.username,self.name,self.email)
    
    # def __str__(self):
    #     return self.__repr__()

class userdatabase:
    def __init__(self):
        self.users = []
        print(self.users)
    
    def insert_user(self,new_user):
        i = 0
        while i < len(self.users):
            if self.users[i].username > new_user.username:
                break
            i += 1
        self.users.insert(i,new_user)
        print(self.users)
    
    def find_user(self,query):
        for user in self.users:
            if user.username == query:
                return user
    
    def update_database(self,query):
        target = self.find_user(query.username)
        target.name, target.email = query.name, query.email
        print(self.users)

        

Jhon = user('Jhon','Jhon Doe','jhondoe@gmail.com')
Mohan = user('Mohan','Mohan Das','mohandas@gmail.com')
Mohan76 = user('Mohan','Mohan Kumar Das','mohandas76@gmail.com')
users = [Jhon,Mohan]
# print(Jhon.name)
# print(Mohan)
# print(users)

database = userdatabase()
database.insert_user(Jhon)
database.insert_user(Mohan)

print(database.find_user(Mohan.username))

database.update_database(Mohan76)
              