from math import sqrt, floor
a = int(input()) #1
b = int(input()) #2
lng = a+b*2
# print(lng)
if(a==0):
    print(floor(lng//4) ** 2)
elif(a%4==0):
    print(max(floor(lng//4) * (floor(lng//4)), (floor((lng-2)//4)) * (floor((lng+2)//4))))
elif(a%4==1):
    print(floor(lng//4) * floor(lng//4))
elif(a%4==2):
    if(lng%4==0):
        print(floor(lng//4) ** 2)
    else:
        print(floor((lng-2)//4) * floor((lng+2)//4))
elif(a%4==3):
    print(floor(lng//4) * floor(lng//4+1))
#err 5, 1
# l1=0
# l2=0
# if(b%4==0):
#     l1 += (b//4)*2
#     l2 += (b//4)*2
# elif(b%4==1):
#     l1 += (b//4)*2
#     l2 += (b//4)*2
# else:
#     l1 += (b//4+1)*2
#     l2 += (b//4)*2
# print(l1, l2)
#
# if(a%4==0):
#     l1 += a//4
#     l2 += a//4
# elif(a%4==1):
#     l1 += a//4
#     l2 += a//4
# else:
#     l1 += a//4
#     l2 += a//4+1
# # k1 = (a//4 + b//4*2)*((a+2)//4 + (b+2)//4*2)
# k1 = ((a+2)//4 + b//4*2)*((a)//4 + (b+2)//4*2)
# k2 = (())
# print(max(k1,k2))
# print(l1,l2,l1*l2)
# if(lng%4==0):
#     k1 = (a//4 + b//4*2)**2
#     print((a//4 + b//4*2))
#     print(1)
# elif(lng%4==2):
#     if(a>0):
#         k1 = (a//4 + b//4*2)*(a//4 + 1 + b//4*2)
#         print((a//4 + b//4*2),(a//4 + 1 + b//4*2))
#         print(2)
#     else:
#         k1 = (a // 4 + b // 4 * 2) ** 2
#         print((a // 4 + b // 4 * 2))
#         print(3)
# else:
#     k1 = (a//4 + b//4*2)**2
#     print((a//4 + b//4*2))
#     print(4)
#     if(lng%4==3):
#         k2 = (a//4 + b//4*2)*(a//4 + 1 + b//4*2)
#         print((a//4 + b//4*2),(a//4 + 1 + b//4*2))
#         print(5)
# if(a-(4*(a//4))>1 and b%4==3):
#     l=1



# k1 = (a//4 + b//4*2 + l)**2
# k2 = 0
# if(a-4*(a//4)>=0 and b-4*(b//4)>=0):
#     print("sfd")
#     k2 = (a//4 + b//4*2 + l)*(a-2*(a//2)+(b-2*(b//2))*2)
#     print(a//4 + b//4*2 + l),(a-2*(a//2)+(b-2*(b//2))*2)
# print(max(k1, k2))