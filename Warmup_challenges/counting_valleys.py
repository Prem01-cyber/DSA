#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    altitude = 0
    valleys = 0
    in_valley = False

    for step in path:
        if step == 'U':
            altitude += 1
        if altitude < 0 and not in_valley:
            in_valley = True
            valleys += 1
        if step == 'D':
            altitude -= 1
        if altitude >= 0 and in_valley:
            in_valley = False
    
    return valleys

# We just need to return valleys
def countingValleys(steps, path):
    valleys = 0
    sea_level = 0

    for step in path:
        if step == 'U':
            sea_level += 1
            if sea_level == 0:
                valleys += 1
        else:
            sea_level -= 1
    return valleys

if __name__ == '__main__':
    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)