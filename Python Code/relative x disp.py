# User Input -------------------------------------------------------------------------------------------------------
file_input = 'ten_lines'
input_file_type = '.txt'
outputFileNameExtension = '_t_x_rel'

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
    with open(file_input + outputFileNameExtension + input_file_type, "w") as wf_txt:
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
                avg_x = sum(list_of_xs) / len(list_of_xs)
                wf_txt.write(str(t_main) + '\t' + str(avg_x) + '\n') # new
                list_of_xs = []

                t_main = t_main + t_step / freq  # counter/freq, counter =+
                # i wrote this whole section again because it skips the first entry of 0.02 sec
                if abs(y - y_relative) <= tol:
                    # list_of_ts_w_xs.append([t, x])
                    list_of_xs.append(x)

            counter = counter + 1

        avg_x = sum(list_of_xs) / len(list_of_xs)
        wf_txt.write(str(t) + '\t' + str(avg_x) + '\n') # new



# This section of code stores a list of the average x displacements of every time stamp of the shake table.
# These values will be subtracted from displacements of the building to get relative displacements of the building
# to its foundation / table.



test = 1

