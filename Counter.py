from collections import Counter;

list = [1,2,3,4,8,4,1,23,6,1,5,4,2,5,3,6,1,7,5]

#Count the freequencies in sorted order and in dict format
cnt = Counter(list) #depends on Value

print(cnt[1])
print(cnt)

cnt = Counter({1:3,2:4})

c={1:2,2:2}
print(c)
cnt.subtract(c)
print(cnt)

cnt.update(c)

p = cnt.elements()

for v in p:
    print(v)


counter = Counter({'a': 3, 'b': 3, 'c': 2})

print(sum(counter.values()))  

print(list(counter)) #TypeError: 'list' object is not callable

print(set(counter))

print(dict(counter))

print(counter.items())

counter = Counter(a=2, b=3, c=-1, d=0)

counter = +counter
print(counter)  

# clear all elements
counter.clear()
print(counter)

list = [1,2,3,4,1,2,6,7,3,8,1]
cnt = Counter(list)
print(cnt.most_common()) #depends on Key

