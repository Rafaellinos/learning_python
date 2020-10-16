

def createTargetArray(nums, index):
    # new_array = []
    # for i, num in zip(index, nums):
    #     new_array.insert(i, num)
    # return new_array

    new_array = [None] * len(index)

    for i in range(len(index)):

        if new_array[index[i]] is not None:

            tmp = new_array[index[i]]
            new_array[index[i]] = nums[i]
            length = len(new_array) - len(new_array[index[i]+1:])

            for idx in range(len(new_array[index[i]+1:])):
                local_tmp = new_array[index[i]+1:][idx]
                new_array[length+idx] = tmp
                tmp = local_tmp
        else:
            new_array[index[i]] = nums[i]
    return new_array


print(createTargetArray(nums=[0, 1, 2, 3, 4], index=[0, 1, 2, 2, 1]))
