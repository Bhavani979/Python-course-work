import numpy as np
print(np)
arr1=np.array([1,2,3,4,5])
print("1-dim",arr1,sep='\n',end='\n\n')
arr2=np.array([[1,2,3],[4,5,6]])
print("2-dim",arr2,sep='\n',end='\n\n')
arr3=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print("multi-dim",arr3,sep='\n')


#To get zeros
zeros=np.zeros((2,4))
print(zeros)

#To get identity matrix
identity=np.eye(4)
print(identity)

#When you want to fill the array with the string
full_array=np.full((2,3),"alphabet")
print(full_array)

#Range of Array
range_arr=np.arange(2,101,2)
print(range_arr)

#Dividing array within the range
lin_space=np.linspace(100,500,5)
print(lin_space)

rand_int=np.random.randint(1,10,(1,30))
print(rand_int)

rand_float=np.random.rand(3,3)
print(rand_float)

rand_norm=np.random.randn(3,3)
print(rand_norm)

rand_choice=np.random.choice(['sunset','beaches','mountains','trecking','resorts'],5)
print(rand_choice)

np.random.seed(42)
rand_arr=np.random.randint(5)
print(rand_arr)

#Checking the shape of array
arr=np.array([[1,2,3],[4,5,6]])
print(arr.shape)

#Reshaping the array
reshaped=arr.reshape(3,2)
print(reshaped)

flattened=arr.flatten()
print(flattened)

transposed=arr.T
print(transposed)

arr=np.array([10,20,30,40,50])
print(arr[0])
print(arr[-1])
print(arr[1:4])
print(arr[:3])
print(arr[::2])

matrix=np.array([[10,20,30],[40,50,60],[70,80,90]])
print(matrix[1,1])
print(matrix[:,0])
print(matrix[0:1,0:2])


arr=np.array([4,9,16,25,36])
print(arr+11)
print(arr**2)
print(arr*2)
print(np.sqrt(arr))


print(np.sum(arr))
print(np.mean(arr))
print(np.median(arr))


print(np.std(arr))
print(np.var(arr))


print(np.min(arr))
print(np.max(arr))


print(np.cumsum(arr))
print(np.cumprod(arr))

arr=np.array([10,20,30,40,50])
bool_arr=arr<25
print(bool_arr)

filtered_arr=arr[arr<25]
print(filtered_arr)

arr=np.array([3,1,4,1,5,9,2,6])
sorted_arr=np.sort(arr)
print(sorted_arr)

unique_vals=np.unique(arr)
print(unique_vals)


