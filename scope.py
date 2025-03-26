# a variable is only available from inside the region it is created is called its scope
# LOCAL SCOPE : avariable created inside a function belongss to the local scope of that function and can only be used inside that function.
x = 300
def myfunc():
#   x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

def mynat():
  print(x)

mynat()