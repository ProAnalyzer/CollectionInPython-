from collections import ChainMap
#Multple Dictionary in a list 

#create a chainMap
dict1 = { 'a' : 1, 'b' : 2 }
dict2 = { 'c' : 3, 'b' : 4 }
chain_map = ChainMap(dict1, dict2)
print(chain_map.maps)
print(chain_map['c'])
print(chain_map['b'])
#As a rule of thumb, when one key appears in more than one associated dictionaries, 
#ChainMap takes the value for that key from the first dictionary.

#Update ChainMaps
dict2['c'] = 5
print(chain_map.maps)

#adding a new dict in chainMap 
dict3 = {'e' : 5, 'f' : 6}
new_chain_map = chain_map.new_child(dict3)
print(new_chain_map)

# reversing the ChainMap 
new_chain_map.maps = reversed(new_chain_map.maps) 
print(new_chain_map)

