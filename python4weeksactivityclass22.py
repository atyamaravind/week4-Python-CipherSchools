file = open("random.txt","w")
file.write("blah blah blah")
file.write("\n new line")
file.close()
file = open("random.txt","w")
file.close()
file = open("random.txt","w")
file.write("jathin katyal")
a = ["jathin","samath","sujith","saransh"]
file.writelines(a)
'''for x in a:
    file.write(x)
file.writelines?'''
file.close()
file = open("sample.txt","r")
'''streams=these are one way readable iterables
==iterables which can iterated in single direction,streams are actually lazy loaded
&streams as a data structure don't have starting point and ending point.
File is also a type of stream'''
print(file.read())
'''moving of a curser==
seek(n):takes the file handle to the n^thbyte from the beginning.'''
'''Context Programming==we write a certain set of a code which has a context or in a
simple way has a value which is just available to these particular names'''
'''python support's context programming&any statement or any syntax in python it works
using dunders the context programming also works on using dunders'''
'''if the context that which was written open("random.txt","r") returns a value we can store the value
in as file:'''
with open("random.txt","r")as file:
    print(file.read())
#print(file.read())

class A:
    def __enter__(self):
        print("Entered")
        return 1
    def __exit__(self,*args):
        print("Excited")
        print(args)
        return True

with A() as x:
    print(x)
    print("inside context")
    raise Exception
print("outside context")
'''JSON files it is nothing but write date in dictionary format to txt
in json values are limited'''
'''keys in json are strings either numbers
-keys can only be stringsb and nubers
-values can only be array, json , numbers, boolean, null'''
a = {
    "name:""Jathin Katyal"
    "marks:""100",
    'languages:'{
        "c++",
        "python",
        "go",
        "rust",
        }
    }
import json
json.dumps()
