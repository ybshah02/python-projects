## Yash Shah
## 0481
import math

#A. 
#==========================================
# Purpose: The function reads the vertices and faces from an OBJ file and transforms the vertices by rotating the model 90 degrees, saved in a new file
# Input Parameter(s):
# fname_in = OBJ file to rotate
# fname_out = OBJ file to save rotated model
# Return Value: returns 0 if the fname_in file exists, returns -1 if the file doesn't exist
#==========================================

def rotate_model(fname_in, fname_out):
    try:
        file_to_rotate = open(fname_in, 'r')
        file_rotated = open(fname_out, 'w')

        for line in file_to_rotate:
            line_cord = line.split()
            if line_cord == []:
                line_cord = line.strip()
            elif line_cord[0] == 'v':
                x = float(line_cord[1])
                y = float(line_cord[2])
                x_rotated = x * math.cos(math.pi/2) + y * math.sin(math.pi/2)
                y_rotated = y * math.cos(math.pi/2) + x * math.sin(math.pi/2)
                line_cord[1] = str(x_rotated)
                line_cord[2] = str(y_rotated)
            line = ' '.join(line_cord)
            file_rotated.write(line + '\n')
            
        file_to_rotate.close()
        file_rotated.close()
        return 0
    except FileNotFoundError:
        return -1

#B. Part 1: get_data_list
#==========================================
# Purpose:
#   Extract the data from a CSV file as a list of rows
# Input Parameter(s):
#   fname is a string representing the name of a file
# Return Value:
#   Returns a list of every line in that file (a list of strings)
#   OR returns -1 if the file does not exist
#==========================================

def get_data_list(fname):

    try:
        data = open(fname, 'r')
        data_list = data.readlines()
        data.close()
        return data_list
            
    except FileNotFoundError:
        return -1

#B. Part 2: get_col_index
#==========================================
# Purpose:
#   Determine which column stores a specific value
# Input Parameter(s):
#   row1_str is a string containing the first row of data 
#   (the column titles) in the CSV file
#	col_title is a string containing the column title
# Return Value:
#   Returns the index of the column specified by col_title
#   OR returns -1 if there is no column found
#==========================================

def get_col_index(row1_str, col_title):
    
    titles = row1_str.split(',')
    if col_title in row1_str:
        col_index = titles.index(col_title)
        return col_index
    else:
        return -1
    

#B. Part 3: convert_dkp
#==========================================
# Purpose:
#   Covert the DKP in your row string to the new system
# Input Parameter(s):
#   row_str is a string containing any row of data from the CSV file
#   idx is an index for the column you want to alter
# Return Value:
#   Returns a string identical to row_str, except with the column
#   at the given index changed to the new DKP (as a string)
#==========================================

def convert_dkp(row_str,idx):
    
    dkp_values = row_str.split(',')
    new_value = float(dkp_values[idx])*13.7
    dkp_values[idx] = str(new_value)
    row_str = ','.join(dkp_values)
    return row_str

#B. Part 4: merge_guild
#==========================================
# Purpose:
#   Alters a DKP CSV file to convert DKP after a guild merger
# Input Parameter(s):
#   fname is the file name of the DKP file
# Return Value:
#   Returns False if the file isn't open
#   Returns False if the file doesn't contain 'DKP' and 'Original Guild' columns
#   Otherwise, returns True
#==========================================

def merge_guild(fname):
    try:
        current_guild = open(fname, 'r')
        current_guild_data = get_data_list(fname)
        
        if 'DKP' in current_guild_data[0] and 'Original Guild' in current_guild_data[0]:
            dkp_col_idx = get_col_index(current_guild_data[0], 'DKP')
            orig_guild_col_idx = get_col_index(current_guild_data[0], 'Original Guild')
        else:
            return False
        
        merged_guild_data = ''
        
        for row in current_guild_data:
            new_row = row
            if get_col_index(row,'Lions of Casterly Rock') == orig_guild_col_idx:
                new_row = row.replace(row, convert_dkp(row, dkp_col_idx))
            merged_guild_data += new_row
            
        current_guild.close()

        merged_guild = open(fname, 'w')
        merged_guild.write(merged_guild_data)
        merged_guild.close()
        
        return True
    except FileNotFoundError:
        return False
