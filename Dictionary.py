from collections import defaultdict

nums = defaultdict(int)
nums['one'] = 1
nums['two'] = 2
print(nums['two'])

print(nums['three'])

count = defaultdict(int)
names_list = "Pronay Ayan Subha Ayan Joy Pronay Ayan Pronay Joy Subha Pronay Ion Naruto Pro ".split()
for names in names_list:
    count[names] +=1
print(count)
print(count["Pronay"])

dd=defaultdict(set)  #set func for eliminate the duplicte
dd['a']={1,2,3,3,2}
print(dd)
print(dd['b'])

from collections import OrderedDict

od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
print(od)

for key, value in od.items():
    print(key, value)

list = ["a","c","c","a","b","a","a","b","c"]
cnt = Counter(list)
od = OrderedDict(cnt.most_common())
for key, value in od.items():
    print(key, value)
    

od3=OrderedDict.fromkeys('akmklslk')
print(od3)
# use of popitem()
q=od3.popitem(last=False)
print(q)
# use of move_to_end()
u=od3.move_to_end('k')
print(od3)
