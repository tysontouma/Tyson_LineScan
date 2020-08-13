# This script was written for the following:
# To take a line scan text file that contains time (in meters) and x and y coordinates
# To filter the text file to specific time periods that the line scan data is of interest
# ****Above comments need to be edited**** 8/12/2020

# The following text file is line scan data from the Kobe Japan 3-story concrete building that was tested on a shake table
# WORKFLOW OF TEXT FILE (done by Tatsu Sweet):
# Leica P50 line scan data was imported into cloud compare, cropped with respect to time (meters) for majority of the
# ... duration when shake test occured. The line scan data was also cropped with respect to the 2-dimensional axes
# ... to include the area of interest. (Raw line scan data is comprised of a 360 degree 2 dimensional plane)

# This script was started by Tyson Touma as an REU with the RAPID Facility (Summer 2020)

from typing import TextIO

from pip._vendor.distlib.compat import raw_input

# this section is user input to where they can choose what file to be read by the code

# file_input = raw_input('Enter the  name of a file you want to read: ')

# User Input -------------------------------------------------------------------------------------------------------
file_input = 't3_lineplot'
input_file_type = '.txt'
step_input = 10
y_relative = -2  # m
tol = 0.01  # m
frequency = 50  # hz
outputFileNameExtension = '_copy'

# output text file is a csv with columns t,x-xt,y
# for each line t = t_in_L/frequency
t = 1
find all the x values for points with y-+tol
    when t = 2
list_of_xs = [x,x,x,x,x]
list_of_xt = [x1,x2,x3,...]
where x1 is the average values for x for t = 1
list_of_xcounts = [2,5,4,3,5,6,7,2,2,3,0,3,4,5,4,2....]
this is a test

# End user input -------------------------------------------------------------------------------------------------------

# this section is user input to where they can choose to decrease the density of the text file



step_count = float(step_input)

# you will see below in the for loop that it always includes line 1 no matter what the step_count is,
# it will then choose what is divisble by the step count.
# For example, step_count = 2, will include line 1, 2, 4, 6, 8, ... etc.

lineCount = 1

with open(file_input + input_file_type, "r") as rf_txt:
    with open(file_input + outputFileNameExtension + input_file_type, "w") as wf_txt:
        for line in rf_txt:
            if lineCount == 1:
                wf_txt.write(line)
                if step_count == 1:
                    wf_txt.seek(0)
            if lineCount % step_count == 0:
                wf_txt.write(line)
            lineCount = lineCount + 1





# *** BELOW is ideas for another script. 8/12/2020

# this is more brainstorming user input, that would change the first column in the text file depending on
# seconds (0.02 intervals) or meters (1 intervals)



