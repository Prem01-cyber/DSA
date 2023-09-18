import math

#Function to find a continuous sub-array which adds up to a given number.

class Solution:
    def subarraySum(self, arr, N, S):
        left = 0
        right = 0
        current_sum = 0

        while right < N:
            current_sum += arr[right]

            while current_sum > S:
                current_sum -= arr[left]
                left += 1

            if current_sum == S:
                return [left + 1, right + 1]  # Adding 1 for 1-based indexing

            right += 1

        return [-1] if S != 0 else [1, 1]  # Handle the case when S is 0



def main():
    T = int(input())
    while(T>0):
        N, S = map(int, input().split())
        A = list(map(int, input().split()))
        ob = Solution()
        ans = ob.subArraySum(A, N, S)
        for i in ans:
            print(i, end=" ")
        print()
        T -= 1

if __name__ == '__main__':
    main()