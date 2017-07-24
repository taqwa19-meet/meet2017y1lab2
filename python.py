Python 3.5.2 (default, Nov 17 2016, 17:05:23) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> a=5
>>> b=10
>>> a=10
>>> b=5
>>> a=5
>>> b=10
>>> a=b
>>> b=a
>>> a
10
>>> a=5
>>> b=10
>>> a=b
>>> a
10
>>> b
10
>>> c=a
>>> a=b
>>> b=c
>>> a
10
>>> b
10
>>> four="4"
>>> rint(four*3)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    rint(four*3)
NameError: name 'rint' is not defined
>>> print(four*3)
444
>>> five=4
>>> print(five)
4
>>> print(five*3)
12
>>> my_name="student"
>>> print("hi,"+  myName)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    print("hi,"+  myName)
NameError: name 'myName' is not defined
>>> print("my name is "+my_name)
my name is student
>>> "hi student"
'hi student'
>>> my_name="student"
>>> print("hi,"+myname")
      
SyntaxError: EOL while scanning string literal
>>> print("hi"+ my_name)
histudent
>>> my_age=15
>>> print("i am "+my_age+"years old)
      
SyntaxError: EOL while scanning string literal
>>> print("i am" my_age "years old "
      
SyntaxError: invalid syntax
>>> print("i am + "my_age"+"years old")
      
SyntaxError: invalid syntax
>>> SyntaxError: invalid sy
SyntaxError: invalid syntax
>>> print("i am"+"my_age"+"years old")
i ammy_ageyears old
>>> my_age=15
>>> print("iam"+"my_age"+"years old)
      
SyntaxError: EOL while scanning string literal
>>> print("i am"+"my_age"+"years old")
i ammy_ageyears old
>>> my_age=15
>>> print("i am"+"15"+"years old")
i am15years old
>>> score=1
>>> total=score+9
>>> score=1
>>> total=score+(count*2)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    total=score+(count*2)
NameError: name 'count' is not defined
>>> total=score+("count"*2)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    total=score+("count"*2)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 
