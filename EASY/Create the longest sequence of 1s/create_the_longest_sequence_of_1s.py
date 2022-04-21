b = input()

one_list = b.split('0')
number_list = [len(one) for one in one_list]

n_max = 0
for i in range(len(number_list)-1):
    n = number_list[i] + number_list[i+1] +1
    if n > n_max: n_max = n
      
print(n_max)
