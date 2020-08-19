
#==========================================
# Purpose: The function takes a list of musical notes and shifts the musical notes' scale based on the number of steps inputed
# Input Parameter(s):
# notes = list of musical notes
# up = number of steps to shift the scale of the list of musical notes
# Return Value(s): a new list of the shifted scale of notes
#==========================================


def convert(notes, up):
    chrom_scale = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    chrom_scale_to_edit = chrom_scale.copy()
    notes_to_change = notes.copy()
    for i in range(0,12):
        chrom_scale_to_edit[i] = -12 + i
    for j in range(len(notes)):
        for k in range(12):
            if notes[j] == chrom_scale[k]:
                notes_to_change[j] = chrom_scale_to_edit[k]
        notes_to_change[j] += (up % 12)
        if notes_to_change[j] > -1:
            notes_to_change[j] -=12
        elif notes_to_change[j] < -12:
            notes_to_change[j] +=12
        for m in range(12):
            if notes_to_change[j] == chrom_scale_to_edit[m]:
                notes_to_change[j] = chrom_scale[m]
    return notes_to_change

#==========================================
# Purpose: The function takes a list of numbers and finds unique combinations of three numbers that equate to a target sum, given by the input
# Input Parameter(s):
# num_lst = list of numbers
# target = target sum for the combinations from the list of numbers 
# Return Value(s): the number of distinct combinations that equate to the target sum
#==========================================

def triple_sum(num_lst, target):
    num_combos = 0
    triple_lst = []
    for i in range(len(num_lst)):
        total_sum = 0
        for j in range(len(num_lst)):
            for k in range(len(num_lst)):
                if num_lst[i] != num_lst[j] and num_lst[j] != num_lst[k] and num_lst[i] != num_lst[k]:
                    new_lst = [num_lst[j], num_lst[i], num_lst[k]]
                    new_lst.sort()
                    total_sum = num_lst[j] + num_lst[i] + num_lst[k]
                    if total_sum == target:
                        triple_lst.append(new_lst)
                        num_combos +=1
                
    for elem in triple_lst:
        while triple_lst.count(elem) > 1:
            triple_lst.remove(elem)
            num_combos-=1
        print(str(elem[0]) + ' + ' + str(elem[1]) + ' + ' + str(elem[2]) + ' = 5 ')               
    return num_combos

#==========================================
# Purpose: The function takes in a list of names, and then orders them in a manner in which all even indexes do not contain the letters s, S, z, or Z
# Input Parameter(s):
# names_list = list of names 
# Return Value(s): a new list of names, ordered in a specified manner explained above or an empty list if there are more names with s,S,z,Z than not
#==========================================

def no_front_teeth(names_list):
    new_names_list = []
    names_without_s_or_z = []
    names_with_s_or_z = []

    for elem in names_list:
        num_char = 0
        for char in elem:
            if char == 's' or char == 'S' or char == 'z' or char == 'Z':
                num_char+=1
        if num_char >=1:
            names_with_s_or_z.append(elem)
        else:
            names_without_s_or_z.append(elem)
            

    if len(names_with_s_or_z) <= len(names_without_s_or_z):
        with_count = 0
        without_count = 0
        for i in range(len(names_list)):
            if i % 2 == 0 or without_count > len(names_with_s_or_z):
                new_names_list.append(names_without_s_or_z[without_count])
                without_count +=1
            else:
                new_names_list.append(names_with_s_or_z[with_count])
                with_count+=1
        return new_names_list
                
    else:
        print("Mission impossible: too many unpronounceable names")
        return new_names_list

