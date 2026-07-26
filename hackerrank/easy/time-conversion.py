# O(1) time and space
# link: https://www.hackerrank.com/challenges/time-conversion

def timeConversion(s):
    hrs = int(s[:2])
    if hrs == 12: hrs = 0
    if s[-2] == 'P': hrs+=12
    return "{:02d}".format(hrs) + s[2:-2]
