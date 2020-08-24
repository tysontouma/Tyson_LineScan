freq = 50
t_main = 0
y_relative = -2
tol = 0.11
list_of_xs = []
list_of_ts_w_xt = []
list_of_ts_w_xs = []

with open('ten_lines.txt', "r") as txt:
    for line in txt:
        row = line.strip("\n").split("\t")
        t_in_l = float(row[0])
        t = t_in_l / freq
        x = float(row[1])
        y = float(row[2])
        # while loop sucks because for loop goes line by line and cant get out of line 1 with while loop
        while t == t_main:
            # list_of_xs = []
            if abs(abs(y) - abs(y_relative)) <= tol:
                ts_w_xs = [t , x]
                list_of_ts_w_xs.append(ts_w_xs)
                list_of_xs.append(x)


    avg_x = sum(list_of_xs) / len(list_of_xs)
    ts_w_xt = [t, avg_x]
    list_of_ts_w_xt.append(ts_w_xt)
    avg_x = 0
    list_of_xs = []

    t_main = t_main + 1/freq
            # i wrote this whole section again because it skips the first entry of 0.02 sec
    # if abs(abs(y) - abs(y_relative)) <= tol:
    #     ts_w_xs = [t , x]
    #     list_of_ts_w_xs.append(ts_w_xs)
    #     list_of_xs.append(x)


print(list_of_ts_w_xt)
print()
print(list_of_ts_w_xs)

