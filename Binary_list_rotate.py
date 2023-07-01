
def rotation_count(list_):
    start,end = 0,len(list_)-1

    while start <= end:
        
        mid = (start+end)//2
        mid_num = list_[mid]

        if mid > 0 and list_[mid] < list_[mid - 1]: # mid number is less than number before that
            return mid
        
        elif list_[mid] < list_[end]: # mid number is less than end, answer lie in left half
            end = mid - 1
        
        elif list_[mid] > list_[end]: # mid number is large than end, answer lie in right half
            start = mid + 1


#test = {'input':{'list_':[5,6,7,1,2,3,4]},'output':3}
#test = {'input':{'list_':[6,7,1,2,3,4,5]},'output':3}
test = {'input':{'list_':[4,5,6,7,1,2,3]},'output':3}

result = rotation_count(test['input']['list_'])
print(result)