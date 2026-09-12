

def commonElement(arr1,arr2):
    return list(set(arr1)& set(arr2))
    # Alternatively, using the .intersection() method
    return list(set(arr1).intersection(arr2))

print(commonElement([1,2,3,4,5,6,7,8],[1,3,5,7])) 


