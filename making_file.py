"""

content = "this is a bunch of content."

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
"""

collection = ["a","b","c","d","e","f","g"]

def linear_search(search_term):
    for x in collection:
        if (x == str(search_term)):
            return True
        return False

print(linear_search("z"))
    


