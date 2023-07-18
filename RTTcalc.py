##
## Python code to remove Calculate RTT for Send+ACK packets
## Author: Luke Herron
## Columbus State University
## Version 1.8.0
## 6/19/2023
##
##
import statistics
import os

def clearFiles():


    def split_t_line(segment, position): #split line into readable parts
        time = segment[:position] #sender side
        return time
    
    def split_line(segment, position): #split line into readable parts
        part1 = segment[:position] #sender side
        part2 = segment[position:] #reciver side
        return part1, part2

    InFileString = "_IN_"
    OutFileSting = "_OUT_"
    position = 39 #at the point of ">"
    hasNoDataString = "[.]" #client port
    hasDataString = "[P.]" #has data
    val_pattern1 = "val"
    
    
    def remove_lines(differences_file, out_and_diff_file, echo_file , outliers_file, input_file, output_file, serverPortString, hasNoDataString, hasDataString, position):
        INFILE = False
        OUTFILE = False
        AWS1 = False
        AWS2 = False
        AWS3 = False
        AWS5 = False
        AWS6 = False
        AWS7 = False
        CCT30 = False
        
        try:
            with open(input_file, 'r') as file:
                lines = file.readlines()
                if InFileString in input_file:
                    print("IN FILE!!!!")
                    INFILE = True
                elif OutFileSting in input_file:
                    print("OUT FILE!!!!")
                    OUTFILE = True 
                    if "AWS1" in input_file:
                        AWS1 = True
                    elif "AWS2" in input_file:
                        AWS2 = True
                    elif "AWS3" in input_file:
                        AWS3 = True
                    elif "AWS5" in input_file:
                        AWS5 = True
                    elif "AWS6" in input_file:
                        AWS6 = True
                    elif "AWS7" in input_file:
                        AWS7 = True
                    elif "CCT30" in input_file:
                        CCT30 = True
                    
            outliers = []
            filtered_lines = []
            differences = []
            echo = []
            diff_out = []
            num_lines = len(lines)
            i = 0
            
            

            while i < num_lines:
                position = 39 #at the point of ">"
                segment = lines[i]
                part1, part2 = split_line(segment, position)
                u = 0
                x = 0
                if serverPortString in part2 and hasDataString in part2:
                    
                    i +=1
                    while u < num_lines and x < 1:
                        position = 39 #at the point of ">"
                        segment1 = lines[u]
                        part1, part2 = split_line(segment1, position)
                        words = segment.split()  # Split the line into individual words
                        index1 = words.index(val_pattern1)  # Find the index of the search string
                        if index1 < len(words) - 1:  # Check if there is a next word
                            digits = words[index1 + 1]  # Get the next word
                            
                        if hasNoDataString in segment1 and digits in segment1 and serverPortString in part1:
                            position = 18
                            time1 = split_t_line(segment, position)
                            time2 = split_t_line(segment1,position)
                            time1 = time1.strip()
                            time2 = time2.strip()
                            try:
                                value = int(time1.replace(".", ""))
                                value2 = int(time2.replace(".", ""))
                                difference = value2 - value
                                diff_out.append(str(difference))
                                if INFILE is True:
                                    if difference < 0 or difference > 50:
                                        outliers.append(lines[i-1])
                                        outliers.append(lines[u])
                                    elif difference >0 and difference < 50:
                                        differences.append(str(difference))
                                        filtered_lines.append(lines[i-1])                           
                                        filtered_lines.append(lines[u])
                                elif OUTFILE is True:
                                    if AWS1 is True:
                                        if difference >80000 and difference < 90000:
                                            differences.append(str(difference))
                                            filtered_lines.append(lines[i-1])                           
                                            filtered_lines.append(lines[u])
                                        else:
                                            outliers.append(lines[i-1])
                                            outliers.append(lines[u]) 
                                    elif AWS2 is True:
                                        if difference >14000 and difference < 19000:
                                            differences.append(str(difference))
                                            filtered_lines.append(lines[i-1])                           
                                            filtered_lines.append(lines[u])
                                        else:
                                            outliers.append(lines[i-1])
                                            outliers.append(lines[u]) 
                                    elif AWS3 is True:
                                        if difference >70000 and difference < 80000:
                                            differences.append(str(difference))
                                            filtered_lines.append(lines[i-1])                           
                                            filtered_lines.append(lines[u])
                                        else:
                                            outliers.append(lines[i-1])
                                            outliers.append(lines[u]) 
                                    elif AWS5 is True:
                                        if difference >130000 and difference < 165000:
                                            differences.append(str(difference))
                                            filtered_lines.append(lines[i-1])                           
                                            filtered_lines.append(lines[u])
                                        else:
                                            outliers.append(lines[i-1])
                                            outliers.append(lines[u]) 
                                    elif AWS6 is True:
                                        if difference >190000 and difference < 220000:
                                            differences.append(str(difference))
                                            filtered_lines.append(lines[i-1])                           
                                            filtered_lines.append(lines[u])
                                        else:
                                            outliers.append(lines[i-1])
                                            outliers.append(lines[u]) 
                                    elif AWS7 is True:
                                        if difference >100000 and difference < 2000000:
                                            differences.append(str(difference))
                                            filtered_lines.append(lines[i-1])                           
                                            filtered_lines.append(lines[u])
                                        else:
                                            outliers.append(lines[i-1])
                                            outliers.append(lines[u]) 
                                    elif CCT30 is True:
                                        if difference >15000 and difference < 18000:
                                            differences.append(str(difference))
                                            filtered_lines.append(lines[i-1])                           
                                            filtered_lines.append(lines[u])
                                        else:
                                            outliers.append(lines[i-1])
                                            outliers.append(lines[u]) 
                                    
                                        
                            except ValueError:
                                print(f"Skipping invalid value: {time1} or {time2}")
                            
                            
                            x += 2
                            
                            continue
                        
                        else:
                            u += 1
                        
                else:
                    echo.append(lines[i])
                    i +=1
                
            with open(out_and_diff_file, 'w') as file:
                file.write('\n'.join(diff_out))   

            with open(output_file, 'w') as file:
                file.write(''.join(filtered_lines))

            with open(outliers_file, 'w') as file:
                file.write(''.join(outliers))

            with open(differences_file, 'w') as file:
                file.write('\n'.join(differences))

            with open(echo_file, 'w') as file:
                file.write('\n'.join(echo))
            
            return output_file  # Return the output file path
    
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Error: File '{input_file}' not found.") from e
        except PermissionError as e:
            raise PermissionError(f"Error: Permission denied for file '{output_file}'. Please check file permissions.") from e

    def process_files(input_files, position, serverPortString, hasNoDataString, hasDataString):
        output_files = []
        differences_files = []
        outliers_files = []
        echo_files = []
        outlier_and_diff_files =[]
        for input_file in input_files:
            output_file = '_Fin_Output_' + input_file #output file name
            differences_file = 'difference_output_' + input_file
            outliers_file = 'Outlier_output_' + input_file
            echo_file = 'Echo_output_' + input_file
            out_and_diff_file = "Outlier_and_diff_" +input_file
            try:
                output_path = remove_lines(differences_file, out_and_diff_file, echo_file, outliers_file, input_file, output_file, serverPortString, hasNoDataString, hasDataString, position)  #call remove lines function
                output_files.append(output_path)  # Append the output file path to the list
            except FileNotFoundError as e:
                print(e)
            except PermissionError as e:
                print(e)
        return output_files , differences_files, outliers_files , echo_files, outlier_and_diff_files


    input_files =[]  #grab differeneces files
    current_directory = os.getcwd()
    files = os.listdir(current_directory)
    inFiles1= "AWS"
    inFiles2 = "CCT30"
    inFiles3 = "Test"
    Echo1 = "Echo"
    difference1 = "difference"
    fin1 = "_fin_"
    outlier1 = "Outlier"
    for file in files:
        if os.path.isfile(file):
            if inFiles1 in file or inFiles2 in file:
                if inFiles3 in file:
                    if Echo1 in file or difference1 in file or fin1 in file or outlier1 in file:
                        print("Did not run: " + file)
                    else:
                        input_files.append(file)
    serverPortString = ".22" #server port
    hasNoDataString = "[.]" #client port
    hasDataString = "[P.]" #has data
    output_files = process_files(input_files, position, serverPortString, hasNoDataString, hasDataString)  #process the files
    
    return output_files

def calculate_stDev(differences, mean):
    
    std_Dev = statistics.stdev(differences)
    
    lower_bound = mean - std_Dev
    upper_bound = mean + std_Dev

    count_within = 0
    count_lower = 0
    count_upper = 0

    for value in differences:
        if lower_bound <= value <= upper_bound:
            count_within += 1
        elif value < lower_bound:
            count_lower += 1
        elif value > upper_bound:
            count_upper += 1

    percentage_within = (count_within / len(differences)) * 100
    percentage_lower = (count_lower / len(differences)) * 100
    percentage_upper = (count_upper / len(differences)) * 100

    return std_Dev, lower_bound, upper_bound, percentage_within, percentage_lower, percentage_upper

def calculate_difference(file_path):
    values = []
    with open(file_path, 'r') as file:
        for line in file:
            try:
                value = float(line.strip())
                values.append(value)
            except ValueError:
                # Ignore non-numeric lines
                pass
    return values

def calculate_mean(differences):
    if len(differences) == 0:
        return None

    total = sum(differences)
    mean = total / len(differences)
    return mean

def main():

# List of file paths
    output_files, differnces_files, outlier_and_diff_files, outliers_files, echo_files = clearFiles() #find outliers, filtered lines, echos, and differences
    print("End of first segment")
    print(output_files)
    print(outliers_files)
    print(differnces_files)

    file_paths =[]  #grab differeneces files
    current_directory = os.getcwd()
    files = os.listdir(current_directory)
    dOutPut = "difference_output_"
    for file in files:
        if os.path.isfile(file):
            if dOutPut in file:
                file_paths.append(file)

    for file_path in file_paths:  #find Standard Deviations
        try:
            differences = calculate_difference(file_path)
            mean = calculate_mean(differences)
            if len(differences) > 1:
                std_Dev, lower_bound, upper_bound, percentage_within, percentage_lower, percentage_upper = calculate_stDev(
                differences, mean)
                newFile = "StDev_" + file_path
                with open(newFile, 'w') as file:
                    file.write("Standard Deviation: " + str(std_Dev))
                    file.write("\nPercentage Within STD_Dev: " + str(percentage_within))
                    file.write("\nPercentage Above Higher Limit: " + str(percentage_upper))
                    file.write("\nPercentage Below Lower Limit: " + str(percentage_lower))
                    print(newFile + "Has been written")
                
        except FileNotFoundError:
            print(f"File not found: {file_path}. Skipping...")

main()
