# Creating a recursive function
def tower_of_hanoi(disks, source, auxiliary, target):
    if (disks == 1):
        print(f'Move disk 1 from rod {source} to rod {target}.')
        return
    # function call itself
    tower_of_hanoi(disks - 1, source, target, auxiliary)
    print(f'Move disk {disks} from rod {source} to rod {target}.')
    tower_of_hanoi(disks - 1, auxiliary, source, target)


disks = int(input('Enter the number of disks: '))
# We are referring source as A, auxiliary as B, and target as C
tower_of_hanoi(disks, 'A', 'B', 'C')  # Calling the function
