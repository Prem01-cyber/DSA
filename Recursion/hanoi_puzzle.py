# Tower of hanoi puzzle

# Rules
# 1. Only one disk can be moved at a time.
# 2. No larger disk may be placed on top of a smaller disk.

def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print('Move disk 1 from {} to {}'.format(source, destination))
        return
    tower_of_hanoi(n-1, source, destination, auxiliary)
    print('Move disk {} from {} to {}'.format(n, source, destination))
    tower_of_hanoi(n-1, auxiliary, source, destination)

# Recursive solution
# 1. Move n-1 disks from source to auxiliary
# 2. Move nth disk from source to destination
# 3. Move n-1 disks from auxiliary to destination

if __name__ == '__main__':
    tower_of_hanoi(3, 'A', 'B', 'C')