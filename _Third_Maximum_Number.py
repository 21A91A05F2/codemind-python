def third_max_num(my_num):
   my_result = [float('-inf'), float('-inf'), float('-inf')]
   for num in my_num:
      if num not in my_result:
         if num > my_result[0]: my_result = [num, my_result[0], my_result[1]]
         elif num > my_result[1]: my_result = [my_result[0], num, my_result[1]]
         elif num > my_result[2]: my_result = [my_result[0], my_result[1], num]
   if float('-inf') in my_result:
      print(max(my_num))
   else:
      print(my_result[2])
n=int(input())
my_list = list(map(int,input().split()))
third_max_num(my_list)