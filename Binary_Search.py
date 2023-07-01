# cards = [13,11,10,7,4,3,1,0]
# query = 11
# op = 1

# Time Complexity = O(Log N)
# Space Complexity = O(1)

import time

def locate_cards(cards,query):
#Binary Search or Brute Force
  
    start, end = 0, len(cards) - 1
    
    while start <= end:
        mid = (start + end) // 2
        mid_number = cards[mid]
        print('start={}   end={}   mid= {}   mid_number={}'.format(start,end,mid,mid_number))
        if mid_number == query:
            return mid
        elif mid_number < query:
            end = mid - 1
        elif mid_number > query:
            start = mid + 1
    
    return -1

#Create Test Cases
tests = []
test0 = {'input':{'cards':[13,11,10,7,4,3,1,0],'query':0} ,'output':7}
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
    print('\n\nTEST CASE #{}'.format(testcase_num))
    print('Input:\n{}\n'.format(i))
    print('Expected Output:\n{}'.format(i['output']))
    print('Actual Output:\n{}\n'.format(result))
    if result == i['output']:
        print('TestCase {} Result = Pass'.format(testcase_num,result))
    else:
        print('TestCase {} Result = Fail'.format(testcase_num,result))
    testcase_num =  testcase_num +  1
    end_time = time.time()
    time_duration = (end_time - start_time) * 10**3
    print("execution time = {:.03f}ms\n\n".format(time_duration))
