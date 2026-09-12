

def flatArray(arr):
    result =[]
    for a in arr:
        if type(a) == list:

            result.extend(flatArray(a))
        else:
            result.append(a)    

    return result


print(flatArray([1,[2,3],[4,[5,6],7],8]))    


