#test3 = {'input':{'cards':[5,5,7,7,2,1,1],'query':2} ,'output':2}

import time

#Write your function here

def EdgeCase_Duplicate_Query(cards,query,mid):
    mid_number = cards[mid]
    print('mid={}   mid_number={}'.format(mid,mid_number))
    if mid_number == query:
        if mid_number - 1 >=0  and    cards [mid-1]== query:
            return 'left'
        else:
            return 'found'
    elif mid_number < query:
        return 'left'
    else:
        return 'right'    

def locate_cards(cards,query):
    start,end = 0, len(cards)-1

    while start <= end:
        mid = (start+end) // 2
        print('start={}   end={} '.format(start,end))
        query_result = EdgeCase_Duplicate_Query(cards, query, mid)

        if query_result == 'found':
            return(mid)
        elif query_result == 'left':
            end = mid-1
        elif query_result == 'right':
            start = mid + 1 
    return -1

#Create Test Cases
tests = []
#test0 = {'input':{'cards':[13,11,10,7,4,3,1,0],'query':0} ,'output':7}
#test1 = {'input':{'cards':[7],'query':7} ,'output':0}
#test2 = {'input':{'cards':[5,5,5,7,2,2,1,1],'query':7} ,'output':3}
test3 = {'input':{'cards':[8,8,7,6,5,5,1],'query':5} ,'output':4}
#test4 = {'input':{'cards':[],'query':7} ,'output':''} # Will result in out of index

#tests.append(test0)
#tests.append(test1)
#tests.append(test2)
tests.append(test3)
#tests.append(test4)
testcase_num = 0

print(tests[0]['input'])
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