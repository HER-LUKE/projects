##
##
## Python code to chaff txt files
## Author: Luke Herron
## Columbus State University
## Version 1.0.0
## 7/19/2023
##
##
import random

def chaff(I_file, percent):  
    with open (I_file, 'r') as file:
        lines = file.readlines()
        added_lines = len(lines) * float(percent) #determine num of added lines
        print(added_lines)
        add_lines = []
        add_nums = []               
        places = random.sample(range(1, (len(lines)-2)), int(added_lines))  #create place values
        places = sorted(places) #sort them
        for nums in places:  # create new value 
            F_line = lines[nums]
            S_line = lines[nums + 1]
            M_add_num = (float(F_line) / float(S_line))
            F_max = M_add_num - float(F_line)
            S_max = float(S_line) - M_add_num
            add_num = M_add_num + random.randint(-(F_max), S_max)
            add_nums.append(int(add_num))
        a_places = list(map(lambda x: x + 1, places)) #add one to each place point
        print("Place of added lines: " + str(a_places)) #accuratly show where they are placed in file
        print("Number of added lines: " + str(add_nums))
        y = 0
        z = 0
        while y < (len(lines)): # run while there are more original lines
            if z < len(places): # run if there are more lines to add
                if y == places[z]: #run if it is time to add a line
                    add_lines.append(lines[y])
                    add_lines.append(add_nums[z])
                    print("After line: " + str(y + 1) + " " + str(add_nums[z]) + " was added")
                    z += 1
                    y += 1
                else:
                    add_lines.append(lines[y])
                    y +=1
            else:
                add_lines.append(lines[y])
                y += 1
        new_file = (str(percent) + "_chaff_" + str(I_file))  #add percent value to begining of string
        with open(new_file , 'w') as n_file:
            for add_line in add_lines:
                n_file.write(str(add_line))
def main(percent, file_list):
    percent = '.' + percent
    for file in file_list:
        chaff(file, percent)
percent = '10'
file_list = ['e55_out_AWS1_OUT_Attack1_Test01.txt' , 's55_out_AWS1_OUT_Attack1_Test01.txt']
main(percent)