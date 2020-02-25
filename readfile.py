employee_file = open("fileexample.txt", "r") # modes you can open a file; "r" for read, "w" for write, "a" for append(adding new infor), "r+" for reading and writing.
#print(employee_file.readable()) #confirms whether the file is readable or not.

print(employee_file.read()) #reads the whole file details

#print(employee_file.readline()) #reads the first line

#print(employee_file.readline()) #reads second line
for employee in employee_file.readlines():
    print(employee)
employee_file.close()

#print(employee_file.readlines()) #puts the lines inside an array.

employee_file.close()