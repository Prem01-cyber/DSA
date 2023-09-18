#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

# The issue here we are repeating the same steps over and over again.
# Hence we are getting bribes values more. For instace we are cound 1,2 and 2,1 as two bribes.
# We need to find a way to avoid this
def minimumBribes(q):
    bribes = 0
    for i in range(len(q) -1, -1, -1):
        print(i, q[i])
        if q[i] - (i+1) > 2:
            print('Too chaotic')
            return
        for j in range(max(0, q[i] -2), i):
            if q[j] > q[i]:
                bribes += 1
    print(bribes)

        
            


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)