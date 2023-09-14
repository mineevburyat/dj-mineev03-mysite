from datetime import datetime

startDate = datetime(*[int(item) for item in input().split(' ')])
endDate = datetime(*[int(item) for item in input().split(' ')])
delta = endDate - startDate
print(delta.days, delta.seconds)

month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def get_delta(data2, data1):
    // 980 2 12 10 30 1
    // 980 3 1 10 31 37
    // 0   1 
startDate = [int(item) for item in input().split(' ')]
endDate = [int(item) for item in input().split(' ')]
delta = endDate - startDate
print(delta.days, delta.seconds)
