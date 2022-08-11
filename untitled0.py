# -*- coding: utf-8 -*-
# Get data and store in list 
def getBufferDataData(path):
    buffer_data = []
    
    with open(path, "r") as apple_file:
        apple_reader = apple.reader(apple_file, delimiter=',')
        for row in apple_reader:
            if len(row) > 0:
               buffer_data.append(row)
    apple_file.close()
    
    return buffer_data




 try:
     with open(path, mode="r", newline='') as apple_file: ...
     apple_file.close()
     head = list_apple[0]
     
     if len(list_apple) != 0:
         # print("\n" + bc.FAIL + "* 5+ bc. ENDC + " = NULL")
         print(bc.WARNING + "File content:" + bc.ENDC)
         for h in range(len(head)):
             print("{0:17s} .format(head [h]), end="") 
         print("\n" + "-" * len(head) * 19)
         
         regex = re.compile('[@!#$%^&*() <>? |} {~:]')
         
         for row in range(1, len(list_apple)):
             for el in range(len(list_apple[row])):
                 if list_apple[row] [el] == "":
                     print(bc.FAIL + "{0:17s}".format("" 5) + bc. ENDC+" |", end='')
                 elif regex.search(list_apple[row] [el]):
                     print (bc.FAIL + bc.UNDERLINE + "{0:17s}".format(list_apple [row] [el]) + bc. ENDC + "|", end='')
                 else:
                     print("{0:17s} .format(list_csv[row] [el]), end='')
             print()
    else:
        print (bc.OKCYAN + "File empty !!!" + bc. ENDC)




    
    
    
# Write apple

 def write_apple(path, new_data):
     path_log= "D:\Coding\Python\Python 4BI\Data_ASM2\log.txt"
     
     new_head = new_data[0]
     # Write new data to path_new

     with open(path_new, mode="w", newline='') as new_file:
          new_file_writer = apple.writer (new_file, delimiter=',' for i in range(len(new_data)): quotechar='"', quoting=csv.QUOTE MINIMAL)
          
          if i = 0:
              new_file_writer.writerow(new_head)
          else:
              new_file_writer.writerow(new_data[i])
     new_file.close()
     #Write to log, and inform to screen
     
     with open(path_log, "a", encoding="utf-8", newline='') as log:
          log_content= str(datetime.datetime.now()) + "\t" + str(path_new) + "\n"
          log.write(log_content)
          log.write("-" (len(log_content)) + "\n")
          Log.close()
    
    

#Get data in 2 files add to list
path1_data = getBufferData(path1) # Sale Price
path2_data = getBufferData (path2) # Discount Percentage

# Store new data ofter merge
new_data = []
new_head = []
# Merge data of 2 files to new_data
 for i in range(0, Len (path1_data)):
     new_data.append([])
     for j in range(9):
         if j < 2:
             new_data[i].append(path2_data[i][j])
         elif 2 ≤ j < 4:
             new_data[i].append(path1_data[i][j])
         elif 5 <j:
             new_data[i].append(path2_data[i][j - 3])
     new_head = new_data[0]
     
     
     
     
     
     
def clean_data(path, pattern):
    data = getBufferData(path)
    new_data = []
    
    regex = re.compile('['+ pattern + ']')
    # Clean data
    for i in range(0, len(data)):
        new_data.append([])
        for j in range(len(data[i])):
            if j < 2:
                 if data[i][j] = "";
                    new_data[i].append("NaN")
                 elif regex.search(data[i][j]):
                    data[i][j] = re.sub('['+ pattern + ']','', data[i][j])
                    new_data[i].append(data[i][j])
                 else:
                    new_data[i].append(data[i][j])

            else:
                 if data[i][j]
                      new_data[i].append(0)
                 elif regex.search(data[i][j]):
                     data[i][j] = re.sub('['+ pattern + ']', '', data[i][j])
                     new_data[i].append(data[i][j])
                 else:
                     new_data[i].append(data[i][j])
     
#Override file
write_apple(path, new_data)

#Read file after clean

print("+ File after cleaning: ")
print("\t> Empty space:[" + bc.FAIL + "" = 5 + bc.ENDC+"] will replace by" + bc.OKCYAN + "NaN" + bc.ENDC)
print("\t> Special characters:["+ bc.FAIL + pattern + bc. ENDC+"] will remove")
     
     
     
     
     
