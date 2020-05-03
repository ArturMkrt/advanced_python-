def arr_replace(array):
    array[array%2!=0]=0
    return array

def arr_replace_where(arr):
    return np.where(arr%2==0,0,arr)

def arr_repeat(arr):
    return np.repeat(arr,3)

def arr_join(arr):
    return np.tile(arr,3)

def arr_intersection(arr1,arr2):
    return np.intersect1d(arr1,arr2)

def arr_random(x,y):
    return np.random.uniform(5,10,size=(x,y))