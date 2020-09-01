# User Input -------------------------------------------------------------------------------------------------------
file_input = 'ten_lines'
input_file_type = '.txt'
outputFileNameExtension_minus = '_minus'
outputFileNameExtension = '_copy'

t_min = 0
t_max = 0.1
freq = 50
t_main = t_min
t_step = 1
y_relative = -2  # m
tol = 0.11 # m
list_of_xs = []
list_of_xt = []
list_of_ts_w_xt = []
list_of_ts_w_xs = []

# End user input -------------------------------------------------------------------------------------------------------
counter = 0

with open(file_input + input_file_type, "r") as rf_txt:
    with open(file_input + outputFileNameExtension_minus + input_file_type, "w") as wf_txt:
        for line in rf_txt:
            row = line.strip("\n").split("\t")
            t_in_l = float(row[0])
            t = t_in_l / freq
            x = float(row[1])
            y = float(row[2])

            if t > t_max:  ### TO DO: figure out a command where it breaks out of the whole entire loop
                break

            if abs(t - t_main) < 0.00000001:
                # list_of_xs = []
                if abs(y - y_relative) <= tol:
                    # list_of_ts_w_xs.append([t, x])
                    list_of_xs.append(x)

            # this is when it moves from 0 sec to 0.02 sec
            else:
                avg_x = round(sum(list_of_xs) / len(list_of_xs),8)
                wf_txt.write(str(t_main) + '\t' + str(avg_x) + '\n') # new
                list_of_xs = []

                t_main = t_main + t_step / freq  # counter/freq, counter =+
                # i wrote this whole section again because it skips the first entry of 0.02 sec
                if abs(y - y_relative) <= tol:
                    # list_of_ts_w_xs.append([t, x])
                    list_of_xs.append(x)

            counter = counter + 1

        avg_x = round(sum(list_of_xs) / len(list_of_xs),8)
        wf_txt.write(str(t) + '\t' + str(avg_x) + '\n') # new


counter2 = 0
list_of_x_rel = []
dont_forget_me = False

with open(file_input + input_file_type, "r") as rf_txt2:
    with open(file_input + outputFileNameExtension_minus + input_file_type, "r") as rf_txt3:
        with open(file_input + outputFileNameExtension + input_file_type , "w") as wf_txt2:
            for line in rf_txt3:
                row_sub = line.strip("\n").split("\t")
                t_sub = float(row_sub[0])
                x_sub = float(row_sub[1])
                if dont_forget_me:
                    if abs(t_rel - t_sub) < 0.00000001:
                        x_rel = round(x_orig - x_sub,8)
                        wf_txt2.write(str(t_sub) + '\t' + str(x_rel) + '\t' + str(y_orig) + '\n')
                        # list_of_x_rel.append(x_rel)
                for line in rf_txt2:
                    row_rel = line.strip("\n").split("\t")
                    t_in_l_rel = float(row_rel[0])
                    t_rel = t_in_l_rel / freq
                    x_orig = float(row_rel[1])
                    y_orig = float(row_rel[2])
                    if abs(t_rel - t_sub) < 0.00000001:
                        x_rel = round(x_orig - x_sub,8)
                        wf_txt2.write(str(t_sub) + '\t' + str(x_rel) + '\t' + str(y_orig) + '\n')
                        # list_of_x_rel.append(x_rel)
                    else:
                        dont_forget_me = True
                        break

                    counter2 = counter2 + 1
print(list_of_x_rel)
print(len(list_of_x_rel))
test = 1






# This section of code stores a list of the average x displacements of every time stamp of the shake table.
# These values will be subtracted from displacements of the building to get relative displacements of the building
# to its foundation / table.



test = 1

# QUESTIONS FOR TATSU:
# 1) because of floating my relative x displacements are having too many decimals.I was going to
# use the round function on everything to 8 decimal places (what the original text file has). Thoughts?
# 2) is the "dont_forget_me" part of the code worrysome to you?
# 3) I apologize for all of the variables, any suggestions on to make the code cleaner and tidy it up?