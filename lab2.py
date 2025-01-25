#Boolean - True or False
print(10 > 9) #True
print(10 == 9) #False
print(10 < 9) #False

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#The bool() function allows to evaluate any value, and give True or False in return
print(bool("Hello")) #True
print(bool(15)) #True

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

"""
Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones.
"""

bool("abc") #True
bool(123) #True
bool(["apple", "cherry", "banana"]) #True

#False:
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})


#Object that is made from a class with a __len__ function that returns 0 or False evaluates to False:
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj)) 

#Functions can Return a Boolean
def myFunction() :
  return True

print(myFunction())


def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

#Also built-in functions can return boolean value:
x = 200
print(isinstance(x, int))


#Operators:
print(10 + 5)

"""
Python divides the operators in the following groups:

  — Arithmetic operators
  — Assignment operators
  — Comparison operators
  — Logical operators
  — Identity operators
  — Membership operators
  — Bitwise operators
"""
"""
+ 	Addition	
- 	Subtraction	
* 	Multiplication	
/ 	Division 	
% 	Modulus	
** 	Exponentiation	
// 	Floor division
"""
"""
Assignment operators are used to assign values to variables:

= 	x = 5 	
+= 	x += 3 	
-= 	x -= 3  	
*= 	x *= 3 	
/= 	x /= 3 	
%= 	x %= 3	
//= 	x //= 3	
**= 	x **= 3	
&= 	x &= 3	
|= 	x |= 3	
^= 	x ^= 3 	
>>= 	x >>= 3
<<= 	x <<= 3
:= 	print(x := 3)
"""

"""
Comparison operators are used to compare two values:

== 	Equal 	
!= 	Not equal
> 	Greater than	
< 	Less than
>= 	Greater than or equal to	
<= 	Less than or equal to
"""

"""
Logical operators are used to combine conditional statements:

and — Returns True if both statements are true
or — Returns True if one of the statements is true
not — Reverse the result, returns False if the result is true
"""

"""
Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

is — Returns True if both variables are the same object
is not — Returns True if both variables are not the same object
"""

"""
Membership operators are used to test if a sequence is presented in an object:

in — Returns True if a sequence with the specified value is present in the object	
not in — Returns True if a sequence with the specified value is not present in the object
"""

"""

&  	AND 	Sets each bit to 1 if both bits are 1	
| 	OR 	Sets each bit to 1 if one of two bits is 1
^ 	XOR 	Sets each bit to 1 if only one of two bits is 1
~ 	NOT 	Inverts all the bits
<< 	Zero fill left shift 	Shift left by pushing zeros in from the right and let the leftmost bits fall off
>> 	Signed right shift 	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
"""

#Operator Precedence:

#Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first:
print((6 + 3) - (6 + 3)) 

#Multiplication * has higher precedence than addition +, and therefor multiplications are evaluated before additions:
print(100 + 5 * 3)

"""
Precedence from top to bottom:

()  —  Parentheses 	
**  —  Exponentiation 	
+x  -x  ~x  —  Unary plus, unary minus, and bitwise NOT 	
*  /  //  %  —  Multiplication, division, floor division, and modulus 	
+  -  —  Addition and subtraction 	
<<  >>  —  Bitwise left and right shifts 	
&  —  Bitwise AND 	
^  —  Bitwise XOR 	
|  —  Bitwise OR 	
==  !=  >  >=  <  <=  is  is not  in  not in  —  Comparisons, identity, and membership operators 	
not  —  Logical NOT 	
and  —  AND 	
or  —  OR
"""

#If two or more operators have the same precedence, the expression is evaluated from left to right.
print(5 + 4 - 7 + 3)


#Lists:
#Lists are created using square brackets []:
thislist = ["apple", "banana", "cherry"]
print(thislist)

"""
List items are ordered, changeable, and allow duplicate values.
List items are indexed, the first item has index [0], the second item has index [1] etc.
"""
#Lists allow duplicate values:
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#Length of list
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#Lists can be of any data type:
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
#And allow to contain different data types:
list1 = ["abc", 34, True, 40, "male"]

#data type - 'list'
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#List constructor:
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#Indexes: (starts from 0)
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#Negative indexing means start from the end (-1 last item, -2 second last item)
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#Range of Indexes:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])
print(thislist[-4:-1])


#Check if Item Exists:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#Change Item Value:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#Change a Range of Item Values:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#if more elements than the range are being replaced: 
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#if less elements than the range are being replaced:
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#insert - inserts an item at the specified index:
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#append - adds new item to the end:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#extend - adds items from another list to the current to the end:
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
#allows to append not only list, but any iterable objects (tuple, set, dictionary):
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#remove - removes the specified item:
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
#if there is more than 1 items, removes the first occurence;
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#pop - removes the specified index:
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#if there is no specific index, the pop() method removes the last item:
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#del - removes the specified index:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
#and can also delete the list completely:
thislist = ["apple", "banana", "cherry"]
del thislist

#clear - emtpies the list:
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#Loop Through a List.
#for loop:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x) 

#Loop Through the Index Numbers.
#range() and len():
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#while loop:
thislist = ["apple", "banana", "cherry"]
index = 0
while(index < len(thislist)):
  print(thislist[index])
  index += 1

#Looping Using List Comprehension:
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#list comprehension:
#instead of this:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist) 

#we can write this:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

#The Syntax
#newlist = [expression for item in iterable if condition == True]
newlist = [x for x in fruits if x != "apple"]
print(newlist)
newlist = [x for x in fruits] 
print(newlist)
#iterable:
newlist = [x for x in range(10)]
print(newlist)
newlist = [x for x in range(10) if x < 5] 
print(newlist)
newlist = [x.upper() for x in fruits] 
print(newlist)
newlist = ['hello' for x in fruits] 
print(newlist)
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

#sorting lists.
#sort(): (alphanumerically)
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"] #alphabetically
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23] #numerically
thislist.sort()
print(thislist)

#Sort Descending:
#reverse = True:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"] 
thislist.sort(reverse = True)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#Customize Sort Function.
#key = function:
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
#the sort() method is case sensitive:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
#uppercase letters first and then lowercase

#str.lower - change priority
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#Reverse Order.
#reverse():
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

#Copy lists.
#We cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2
#copy():
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
#list():
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
#slice operator ":" :
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

#join two lists:
# + operator:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3) 
#append:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)
print(list1) 
#extend:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1) 

#List methods:
"""
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
"""

#Tuples.
#A tuple is a collection which is ordered and unchangeable. Tuples are written with round brackets ().
thistuple = ("apple", "banana", "cherry")
print(thistuple)
#Tuple items are ordered, unchangeable, and allow duplicate values.
#Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
#len():
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#to create a tuple with one item, it should have a comma after the item
thistuple = ("apple",) #tuple
print(type(thistuple))
#NOT a tuple
thistuple = ("apple") #str
print(type(thistuple))

#Tuple items can be of any data type:
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)\

#A tuple can contain different data types:
tuple1 = ("abc", 34, True, 40, "male")
#type - 'tuple'
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

#tuple():
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

#indexing is the same as in lists!!!

#Change Tuple Values:
#convert into a list method:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x) 
#Add Items.
#convert into a list method:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)
#add tuple to tuple:
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

#Remove items.
#convert into a list method:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
#del - delete a tuple completely:
thistuple = ("apple", "banana", "cherry")
del thistuple
#print(thistuple) this will raise an error because the tuple no longer exists 

#Unpacking a Tuple.
#packing a tuple:
fruits = ("apple", "banana", "cherry")
#But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
#The number of variables must match the number of values in the tuple, if not, it must use an asterisk to collect the remaining values as a list.

#Asterisk*:
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
#----
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

#Loop tuples the same as in lists!!!

#Join tuples the same as in lists!!!
#Note: new — multiplication of lists/tuples etc.

#Tuple methods: (only two)
"""
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found
"""

#Sets
#A set is a collection which is unordered, unchangeable*, and unindexed.
#Set items are unchangeable, but you can remove items and add new items.
#Sets are written with curly brackets {}.
thisset = {"apple", "banana", "cherry"}
print(thisset) 
#Sets are unordered, so you cannot be sure in which order the items will appear.
#Set items are unordered, unchangeable, and do not allow duplicate values.
#Once a set is created, you cannot change its items, but you can remove items and add new items
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

#The values True and 1 are considered the same value in sets, and are treated as duplicates:
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

#The values False and 0 are considered the same value in sets, and are treated as duplicates:
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)

#len():
thisset = {"apple", "banana", "cherry"}
print(len(thisset)) 

#Set items can be of any data type:
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False} 
#A set can contain different data types:
set1 = {"abc", 34, True, 40, "male"} 
#type - 'set'
myset = {"apple", "banana", "cherry"}
print(type(myset))
#The set() Constructor:
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

#You cannot access items in a set by referring to an index or a key. 
#But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
#For loop the same as in lists/tuples!!!

#to add items used add() method:
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")
print(thisset) 

#To add items from another set into the current set, use the update() method.
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset) 

#The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)
print(thisset)

#To remove an item in a set, use the remove(), or the discard() method.
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana") #remove method
print(thisset)
# If the item to remove does not exist, remove() will raise an error.

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana") #discard method
print(thisset) 
#If the item to remove does not exist, discard() will NOT raise an error.

#You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.
#The return value of the pop() method is the removed item.
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()
print(x)
print(thisset) 

#The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}

thisset.clear()
print(thisset) 

#The del keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}

del thisset
# print(thisset) 

#for loop with sets:
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x) 

#Join sets:
"""
There are several ways to join two or more sets in Python.

The union() and update() methods joins all items from both sets.
The intersection() method keeps ONLY the duplicates.
The difference() method keeps the items from the first set that are not in the other set(s).
The symmetric_difference() method keeps all items EXCEPT the duplicates.
"""

#Union:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3) 
#You can use the | operator instead of the union() method, and you will get the same result.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3) 

#Join Multiple Sets.
#Join multiple sets with the union() method:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset) 

#Use | to join two sets:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset) 

"""
The union() method allows you to join a set with other data types, like lists or tuples.
The result will be a set.
"""
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z) 
#The  | operator only allows you to join sets with sets, and not with other data types like you can with the  union() method.

#Update.
#The update() method inserts all items from one set into another.
#The update() changes the original set, and does not return a new set.
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1) 
#Both union() and update() will exclude any duplicate items.


#Intersection:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

#You can use the & operator instead of the intersection() method, and you will get the same result
#Use & to join two sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3) 
#The & operator only allows you to join sets with sets, and not with other data types like you can with the intersection() method.

#The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)
print(set1)

set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2)
print(set3)


#Difference:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)
print(set3) 

#You can use the - operator instead of the difference() method, and you will get the same result.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3) 
#The - operator only allows you to join sets with sets, and not with other data types like you can with the difference() method.

#The difference_update() method will also keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)
print(set1) 


#Symmetric Differences:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)
print(set3) 

#You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3) 
#The ^ operator only allows you to join sets with sets, and not with other data types like you can with the symmetric_difference() method.

#The symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)
print(set1) 


"""
add() 	  	                    Adds an element to the set
clear() 	  	                  Removes all the elements from the set
copy() 	  	                    Returns a copy of the set
difference() 	                  - 	Returns a set containing the difference between two or more sets
difference_update() 	          -= 	Removes the items in this set that are also included in another, specified set
discard() 	  	                Remove the specified item
intersection() 	                & 	Returns a set, that is the intersection of two other sets
intersection_update() 	        &= 	Removes the items in this set that are not present in other, specified set(s)
isdisjoint() 	  	              Returns whether two sets have a intersection or not
issubset() 	                    <= 	Returns whether another set contains this set or not
  	                            < 	Returns whether all items in this set is present in other, specified set(s)
issuperset() 	                  >= 	Returns whether this set contains another set or not
  	                            > 	Returns whether all items in other, specified set(s) is present in this set
pop() 	  	                    Removes an element from the set
remove() 	  	                  Removes the specified element
symmetric_difference() 	        ^ 	Returns a set with the symmetric differences of two sets
symmetric_difference_update() 	^= 	Inserts the symmetric differences from this set and another
union()                       	| 	Return a set containing the union of sets
update() 	                      |= 	Update the set with the union of this set and others
"""


#Dictionaries.
#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
#Dictionaries are written with curly brackets, and have keys and values:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
#Dictionary items are ordered, changeable, and do not allow duplicates.
#Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

#Dictionaries cannot have two items with the same key:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict) 

#lem():
print(len(thisdict))

#The values in dictionary items can be of any data type:
thisdict =	{
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
} 
#type - 'dict'
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict)) 
#The dict() Constructor:
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

#Accessing Items.
#You can access the items of a dictionary by referring to its key name, inside square brackets:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)

#There is also a method called get() that will give you the same result:
x = thisdict.get("model")
print(x)

#Get Keys.
#The keys() method will return a list of all the keys in the dictionary.
x = thisdict.keys()
print(x)

#The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change

#Get Values.
#The values() method will return a list of all the values in the dictionary.
x = thisdict.values() 
print(x)

#The list of the values is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the values list.
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()
print(x) #before the change
car["year"] = 2020
print(x) #after the change 


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()
print(x) #before the change
car["color"] = "red"
print(x) #after the change 

#Get Items.
#The items() method will return each item in a dictionary, as tuples in a list.
x = thisdict.items() 
print(x)

#The returned list is a view of the items of the dictionary, meaning that any changes done to the dictionary will be reflected in the items list.
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()
print(x) #before the change
car["year"] = 2020
print(x) #after the change 


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()
print(x) #before the change
car["color"] = "red"
print(x) #after the change 

#Check if Key Exists.
#To determine if a specified key is present in a dictionary use the in keyword:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary") 

#Change Values.
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict)

#Update Dictionary
#The update() method will update the dictionary with the items from the given argument.
#The argument must be a dictionary, or an iterable object with key:value pairs.
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020}) 
print(thisdict)

#Adding Items.
#Adding an item to the dictionary is done by using a new index key and assigning a value to it:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

#update():
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"}) 

#Removing Items.
#The pop() method removes the item with the specified key name:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict) 

#The popitem() method removes the last inserted item:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict) 

#The del keyword removes the item with the specified key name:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict) 

#The del keyword can also delete the dictionary completely:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
#print(thisdict) this will cause an error because "thisdict" no longer exists. 

#The clear() method empties the dictionary:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict) 

#Loop Through a Dictionary.
#When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.
#Print all key names in the dictionary, one by one:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x) 

#Print all values in the dictionary, one by one:
for x in thisdict:
  print(thisdict[x]) 

#values() for retrieving values:
for x in thisdict.values():
  print(x) 

#keys() for retrieving keys:
for x in thisdict.keys():
  print(x) 

#Loop through both keys and values, by using the items() method:
for x, y in thisdict.items():
  print(x, y) 


#Copy a Dictionary
#You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.
#There are ways to make a copy, one way is to use the built-in Dictionary method copy()
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)
#Another way to make a copy is to use the built-in function dict().
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict) 


#Nested Dictionaries.
#A dictionary can contain dictionaries, this is called nested dictionaries.
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
} 
print(myfamily)

#Or, if you want to add three dictionaries into a new dictionary:
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
} 
print(myfamily)

#Access Items in Nested Dictionaries:
#To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary:
print(myfamily["child2"]["name"]) 

#Loop Through Nested Dictionaries.
#You can loop through a dictionary by using the items() method like this:
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])

#Dict methods:
"""
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
"""