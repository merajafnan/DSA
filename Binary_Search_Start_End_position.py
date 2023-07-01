test = {'input':{'cards':[1,2,8,8,8,9,9,9,10,15],'query':8},'output':6}

def edge_case(cards,query,mid):
    
    mid_num = cards[mid]
    print('mid {}   mid_number {}'.format(mid,mid_num))
    if mid_num == query:
        if cards[mid -1] >=0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_num < query:
        return 'right'
    else:
        return 'left'

def locate_cards_first(cards,query):
    start,end = 0, len(cards)-1
    
    while start <= end:
        mid = (start+end) // 2
        print('start {}   end {}'.format(start,end))
        query_result = edge_case(cards,query,mid)

        if query_result == 'found':
            return(mid)
        if query_result == 'left':
            end = mid -1
        if query_result == 'right':
            start = mid + 1
    return -1

def locate_cards_last(cards,query):
    start,end = 0,len(cards)-1

    while start <= end:
        mid = (start+end) // 2
        mid_number = cards[mid]

        if mid_number == query:
            return(mid)
        elif mid_number > query:
            end = mid - 1
        elif mid_number < query:
            start = mid + 1 
    return -1
            
#test = {'input':{'cards':[1,2,3,5,8,9,10,11,12,15],'query':8},'output':6}

first = locate_cards_first(**test['input'])
last = locate_cards_last(**test['input'])

print('\nFirst_Position {}   Last_Position {}'.format(first,last))
