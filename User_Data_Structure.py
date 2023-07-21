#Create a DS containing 100 miliion record and perform insertion, search, update and list operation effeciently.

class user:
    def __init__(self, username,name,email):
        self.username = username
        self.name = name
        self.email = email
        print('User Created')
    def __repr__(self):
        return "(useranme = {},name = {}, email = {})".format(self.username,self.name,self.email)
    def __str__(self):
        return self.__repr__()

user1 =  user('Jhon','jhon doe','jhondoe@gmail.com')
print(user1,'\n',user1.name)