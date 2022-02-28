

content = "this ais a bunch of content."

content += "\nHere is some content."

file = open("test.txt", "w") #opening the file stream in 'write' mode
file.write("this is a bunch of test text,") # writing text to a file
file.close() #closing file string


file = open("test.txt","r")
print(file.read())
file.close()

file = open("test.txt","a")
file.write("this is some extra stuff that has been added")
file.close()
