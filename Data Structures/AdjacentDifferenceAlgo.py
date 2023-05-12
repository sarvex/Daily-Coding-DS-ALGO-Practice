# Python code to demonstrate
# to calculate difference
# between adjacent elements in list

# Size of List
n = int(input("Enter the size of List : "))

ini_list = [int(input()) for _ in range(0,n)]
# printing ini_list
print("intial_list", ini_list)

diff_list = [y-x for x, y in zip(ini_list[:], ini_list[1::])]
# printing difference list
print("difference list: ", diff_list)
