# users = {'hello':"world","my":"life","alter":"reality"}

# mylist =[{'fgf':'fgf','gfgf':'gfgf'}]

# obj = {
#     "fgfd":"fgdfgd"
# }

# for item in users.items() :
#     print(item)
#     print(type(item))
# print(type(mylist))
# print(sum(range(4)))
s = 'ab'
slen = len(s)
# res = []
# for i in range(0, slen, 2):
#     res.append(s[i:i+2])
# if slen % 2 != 0:
#     res[-1] = res[-1] + '_' # last element in list

# 3, 4 5,6 7 8 9 

res = [s[i:i+2] if i+1 < slen else s[i]+'_' for i in range(0,slen,2)]

def tribonacci(signature, n):
    # arr = []
    # arr = signature.copy() 
    # if n <= 2:
    #     return signature[0:n]
    # for i in range(3,n):
    #     arr.append(arr[i-1]+arr[i-2]+arr[i-3])
    # print(arr)
    arr = [1,1,1]
    arr = arr +  [arr[i-1]+arr[i-2]+arr[i-3] for i in range(3,n)]
    print(arr)
    return arr
    #return signature[:n] + [sum(signature[i-3:i]) for i in range(3, n)]



print(tribonacci([1,1,1],10))





# print(res)

