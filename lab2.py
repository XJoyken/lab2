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