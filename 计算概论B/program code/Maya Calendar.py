month = ['pop', 'no', 'zip', 'zotz', 'tzec', 'xul', 'yoxkin', 'mol', 'chen', 'yax', 'zac', 'ceh', 'mac',
         'kankin', 'muan', 'pax', 'koyab', 'cumhu', 'uayet']
day = ['imix', 'ik', 'akbal', 'kan', 'chicchan', 'cimi', 'manik', 'lamat', 'muluk', 'ok', 'chuen',
       'eb', 'ben', 'ix', 'mem', 'cib', 'caban', 'eznab', 'canac', 'ahau']
n = int(input())
print(n)
for _ in range(n):
    str1 = list(input().split(' '))
    str1[0] = str1[0].strip('.')
    days = int(str1[0])
    days += 20 * month.index(str1[1]) + 365*int(str1[2]) + 1
    years = (days-1) // 260
    days = days % 260
    print(days % 13 if days % 13 else '13', day[days % 20-1], years)
