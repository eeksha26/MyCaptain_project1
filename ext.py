x=input("Input the filename:")
dict={'.py':'python','.c':'C','.java':'Java','.txt':'text'}
a=x.index(".")
str=x[a:]
print("The extension of the file is {}".format(dict.get(str)))
