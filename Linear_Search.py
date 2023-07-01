# cards = [13,11,10,7,4,3,1,0]
# query = 7
# op = 3

import time

def locate_cards(cards,query):
                                        #Linear Search or Brute Force
    position = 0
    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1         
    return -1

#Create Test Cases
tests = []
test0 = {'input':{'cards':[13,11,10,7,4,3,1,0],'query':7} ,'output':3}
test1 = {'input':{'cards':[7],'query':7} ,'output':0}
test2 = {'input':{'cards':[5,5,5,7,2,2,1,1],'query':7} ,'output':3}
test3 = {'input':{'cards':[5,5,7,7,2,1,1],'query':7} ,'output':2}
test4 = {'input':{'cards':[],'query':7} ,'output':''} # Will result in out of index

tests.append(test0)
tests.append(test1)
tests.append(test2)
tests.append(test3)
tests.append(test4)
testcase_num = 0

#print(tests)
for i in tests:
    start_time = time.time()
    result = locate_cards(**i['input'])
    print('TestCase{} = {}'.format(testcase_num,i))
    if result == i['output']:
        print('TestCase{} = Pass\nQuery Position = {}'.format(testcase_num,result))
    else:
        print('TestCase{} = Fail\nQuery Position = {}'.format(testcase_num,result))
    testcase_num =  testcase_num +  1
    end_time = time.time()
    time_duration = (end_time - start_time) * 10**3
    print("execution time = {:.03f}ms\n\n".format(time_duration))
