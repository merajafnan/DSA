def rotation_count(list_):
    print('List : {}'.format(list_))

    position = 0
    while position < len(list_):
        if position > 0    and   list_[position] < list_[position-1]:
            return position
        else:
            position += 1
    return -1
#test = {'input':{'list_':[5,6,7,1,2,3]},'output':3}
test = {'input':{'list_':[1,2,3,4]},'output':3}

result = rotation_count(test['input']['list_'])
print('Number of rotation : {}'.format(result))
#result = rotation_count(2,3)