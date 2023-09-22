n = int(input())
s = set(map(int, input().split()))
N = int(input())

# Remove, discard, pop
while N>0:
    N -= 1
    command = input().split()
    if command[0] == 'pop':
        s.pop()
    elif command[0] == 'remove':
        s.remove(int(command[1]))
    elif command[0] == 'discard':
        s.discard(int(command[1]))
    else:
        print("Invalid command")
print(sum(s))

# Union
n1 = int(input())
s1 = set(map(int, input().split()))
n2 = int(input())
s2 = set(map(int, input().split()))

print(len(s1.union(s2)))

# Intersection
n1 = int(input())
s1 = set(map(int, input().split()))
n2 = int(input())
s2 = set(map(int, input().split()))

print(len(s1.intersection(s2)))

# Difference
n1 = int(input())
s1 = set(map(int, input().split()))
n2 = int(input())
s2 = set(map(int, input().split()))

print(len(s1.difference(s2)))

# Symmetric Difference
# returns a set with all the elements that are in the set and the iterable but not both.
n1 = int(input())
s1 = set(map(int, input().split()))
n2 = int(input())
s2 = set(map(int, input().split()))

print(len(s1.symmetric_difference(s2)))

# Update, Intersection_update, Difference_update, Symmetric_difference_update