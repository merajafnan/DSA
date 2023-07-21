# 1. BINARY SEARCH

# def locate_cards(card,query):
#     start,end = 0,len(card)-1

#     while start <= end:
#         mid = (start+end) // 2
#         print("Card={}\nQuery={}\nMid={}".format(card,query,mid))
        
#         query_result = duplicate_cases(card,query,mid)
#         if query_result == 'found':
#             return mid
#         elif query_result == 'right':
#             start = mid +1
#         elif query_result == 'left':
#             end = mid -1
#     return -1
            

# def duplicate_cases(card,query,mid):
#     mid_number = card[mid]
#     print("Mid_Number={}\n".format(mid_number))
    
#     if mid_number == query:
#         if mid_number-1 >=0 and card[mid-1] == query:
#             return 'left'
#         else:
#             return 'found'
#     elif mid_number > query:
#         return 'left'
#     else:
#         return 'right'
        


# card = [2,5,5,7,7,8,8,9,10]
# query = 9

# result = locate_cards(card,query)
# print("\nCard_Location_Result={}\n".format(result))

##################################################################################################################

# 2. Rotation



# def rotation_count(list1):
#     start,end = 0,len(list1)-1

#     while start <= end:
#         mid = (start+end) // 2

#         if mid > 0      and     list1[mid] < list1[mid-1]:
#             return mid
#         elif list1[mid] < list1[end]:
#             end = mid - 1
#         elif list1[mid] > list1 [end]:
#             start = mid + 1

# #test = {'input':{'list_':[5,6,7,1,2,3,4]},'output':4}
# #test = {'input':{'list_':[6,7,1,2,3,4,5]},'output':3}
# # test = {'input':{'list_':[5,6,7,1,2,3]},'output':5}

# list1 = [5,6,7,1,2,3]
# result = rotation_count(list1)
# print(result)



######################################################################################################

# class user:
#     def __init__(self,username,name,email):
#         self.username = username
#         self.name = name
#         self.email = email
    
#     def __repr__(self):
#         return("Username={} Name={} Email={}".format(self.username,self.name,self.email))
    
# class userdatabase:
#     def __init__(self):
#         self.contact_book = []   # afnan,meraj,zaid,sohan
    
#     def insert_user(self,new_user):
#         i = 0
#         while i < len(self.contact_book):
#             if self.contact_book[i].username > new_user.username:
#                 break
#             i += 1
#         self.contact_book.insert(i,new_user)
#         print(self.contact_book)

#     def find_user(self,user):
#         i = 0
#         for i in self.contact_book:
#             if i.username == user.username:
#                 return i
    
#     def update_database(self,user):
#         target = self.find_user(user.username)
#         target.username,target.email = user.username, user.email


# Meraj = user('Meraj','Meraj Hassan','merajafnan@gmail.com')
# Afnan = user('Afnan','Afnan Meraj','merajafnan@gmail.com')

# database = userdatabase()
# database.insert_user(Meraj)
# database.insert_user(Afnan)

# print(database.find_user(Afnan))

###############################################################################################


