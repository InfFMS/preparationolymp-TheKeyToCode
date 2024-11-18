a = int(input())
b = int(input())
sa = a//2
sb = b//2
k = a - 1 + b - 1 + (max(min(a,b)-1,0)) + max(min(sb,a-sa-1),0) + max(min(sa,b-sb-1),0)
# print( a - 1 , b - 1 , (max(min(a,b)-1,0)) , max(min(sb,a-sa-1),0) , max(min(sa,b-sb-1),0) )
print(k)