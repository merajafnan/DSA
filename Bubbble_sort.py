
import random 
def bubble_sort(shuffled_list):
    nums = list(shuffled_list)
    for j in range(len(nums)-1):
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                nums[i],nums[i+1] = nums[i+1],nums[i]
    return nums

in_list = list(range(-10,10))
out_list = list(range(-10,10))
random.shuffle(in_list)

result = bubble_sort(in_list)

print(' Shuffled list: {} \n Correct List: {} \n B.Sort list: {}'.format(in_list,out_list,result))