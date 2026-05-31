#filerror
try:
    file = open("a_file.txt")
    a_dict = {"key" : "value"}
    print(a_dict["key"])

except FileNotFoundError:
    # print("Error")
    file = open("a_file.txt", "w")
    file.write("something ")

except KeyError as errormessage:
    print(f"the key {errormessage} does not exist")

else:
    content = file.read()
    print(content)

finally: 
    raise KeyError
    # file.close()
    # print("file was closed ")



# with open("a_file.txt") as file:
#     file.read()

#key error
# a_dict = {"key": "value"}
# value = a_dict["non_exists"]

#indexError
# fruit_list = ["apple", "pie"]
# fruits = fruit_list[2]

#typeError
# text = "ABC"
# print(text + 5)

#sytanx Error

# try : something that might cause an Exception

# except : do this if there was an exception 

# else : do this if there we no Exception

# finally : do this no matter what happens 

