# Question 1


def safety_check(report):
    n = len(report)
    if n<2:
        return True
    else:
        if report[0]>report[1]:
            for i in range(n-1):
                if report[i]-report[i+1] not in [1,2,3]:
                    return False
        else:
            for i in range(n-1):
                if report[i+1]-report[i] not in [1,2,3]:
                    return False
    return True

# Time complexity: O(n) where n is the length of each list
# Space complexity: O(n)


def safe_count(data):
    count = 0
    for k in data:
        if safety_check(k):
            count += 1
    return count
# Time complexity: O(Q) where Q is the numbers of integers in the reports
# Space complexity: O(Q)

with open('advent2.txt', 'r') as f:
    liste = [list(map(int,ligne.split())) for ligne in f.readlines()]
print(safe_count(liste))