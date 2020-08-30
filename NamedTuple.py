from collections import namedtuple

#creating
Employee = namedtuple('Employee', 'First_name, Middle_name, Last_name, Age')
e1 = Employee('Pronay', 'Kumar', 'Ghosh', '21')
print(e1.First_name)
print(e1.Middle_name)
print(e1.Last_name)
print(e1.Age)

#creating using list
e2 = Employee._make(['Ayan','Raj','Sharma','18'])
print(e2)

#create a new instance using existing instance
e2 = e1._asdict()   #asdict func is basically an OrderedDict
print(e2)

#Changing field value
e2 = e1._replace(Age='22')
print(e1)
print(e2)

di = { 'First_name' : "Nikhil", 'Middle_name':"Sen",'Last_name':"Sharma",'Age' : 19 }
print(Employee(**di)) # " ** " use if and only if in mapping

#checking the fields
print(e1._fields)

