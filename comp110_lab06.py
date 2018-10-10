"""
Module: comp110_lab06

Modules with some functions for Lab 06 practice problems.
"""
import math
import matplotlib.pyplot as plt

def longest_run(num_list):
    """
    Computes and returns the length of the longest
    run of consecutive equivalent numbers in num_list
    """
    
    current_run_length = 1
    longest_run_length = 1
    for i in range(1,len(num_list)):
        if num_list[i] == num_list[i-1]:
            current_run_length = current_run_length + 1
            if current_run_length > longest_run_length:
                longest_run_length = current_run_length
        else:
            current_run_length = 1

    return longest_run_length

def smooth(num_list):
    """
    Returns a new array that is a copy of
    num_list, but with each element smoothed
    by replacing it with the average of it and 
    the two elements on either side of it.
    You can assume that the length of num_list is
    at least 2.
    """
    ret_list = num_list.copy()

    # Handle the first element of num_list as a special case
    # YOU ADD CODE HERE

    # Handle the second element through the second to last element
    for i in range(1, 2): # YOU ADD CODE HERE, replacing the 1,2, which is a placeholder.
        #    compute the average of the element in num_list at index i and the elements before and after it.
        avg = 0 # YOU ADD CODE HERE, replacing the 0 which is a placeholder.
        #    put the average into index i of ret_list
        # YOU ADD CODE HERE

    #Handle the last element of num_list as a special case
    #YOU ADD CODE HERE

    return ret_list

def read_file(file_name):
    """
    Reads from the file named file_name,
    and creates and returns a list containing
    the difference between the two values on
    each line of the file.
    """

    # open the file
    in_file = open(file_name, "r")

    # create the list to be returned
    ret_list = []

    # iterate over all lines of the file
    for line in in_file:
        # split the line into strings
        strs = line.split()

        # get the numbers out of the list
        num1 = float(strs[0])
        num2 = float(strs[1])

        # compute the difference and put in the list
        ret_list.append(num1 - num2)
    
    # return the list
    return ret_list

def plot_data():
    """
    Illustrates the usage of matplotlib.pyplot module
    """

    # create some x, y data.
    x = [12.4, 14.3, 14.5, 14.9, 16.1, 16.9, 16.5, 15.4, 17, 17.9, 
         18.8, 20.3, 22.4, 19.4, 15.5, 16.7, 17.3, 18.4, 19.2, 17.4, 19.5, 19.7, 21.2]

    y = [11.2, 12.5, 12.7, 13.1, 14.1, 14.8, 14.4, 13.4, 14.9, 15.6, 16.4, 17.7,
         19.6, 16.9, 14, 14.6, 15.1, 16.1, 16.8, 15.2, 17, 17.2, 18.6]
    all_x = list(range(0, 25))

    # plot the data
    plt.plot(x, y, 'b.')
    plt.plot(all_x, all_x, 'r-')
    plt.axis([10, 24, 10, 24])
    plt.xlabel("List Price (in $1000)")
    plt.ylabel("Best Price  (in $1000)")
    plt.title("List versus best selling price for a new GMC pickup")
    plt.show()

def plot_histogram():
    """
    Illustrates making a histogram using the matplotlib.pyplot module
    """

    # create some data.
    x = [12.4, 14.3, 14.5, 14.9, 16.1, 16.9, 16.5, 15.4, 17, 17.9, 
         18.8, 20.3, 22.4, 19.4, 15.5, 16.7, 17.3, 18.4, 19.2, 17.4, 19.5, 19.7, 21.2]

    # make a histogram of the data
    num_bins = 10
    plt.hist(x, num_bins, facecolor='blue', edgecolor='black', alpha=0.5)
    plt.xlabel("List Price (in $1000)")
    plt.title("Frequency of list prices for a new GMC pickup")
    plt.show()


def get_belmont_times(data_file):
    """
    Reads data_file into a dictionary.  The data_file has
    contains one line for each year.  The line contains the year and the
    winning time for that year.  The format for the winning time
    is illustrated by this example: 2:21.20.  This means 2 minutes, 21.2 seconds.
    The dictionary that is created should have the year as key, and the winning
    time as value.
    The created dictionary should be returned.
    """
    winning_times = {}


    return winning_times

def lookup_belmont_time(data_file):
    """
    Reads in the Belmont winning times into a dictionary, then prompts
    the user to enter a year, then looks up and returns the winning time
    for that year.
    """

    return 0   # placeholder.  Replace with actual return value.

def plot_belmont_times(winning_times):
    """
    Makes a plot of the winning belmont times.  winning_times
    is a dictionary where the key is the year, and the value is the
    winning time for that year.
    """

def histogram_belmont_time(winning_times):
    """
    Makes a histogram plot of the winning belmont times.  

    """

def mean(alist):
    """
    Computes and returns mean of the values in alist
    """
    mean = sum(alist) / len(alist)
    return mean

def standardDev(alist):
    """
    Computes and returns standard deviation of the values in alist
    """    
    the_mean = mean(alist)
    
    total = 0
    for item in alist:
        difference = item - the_mean
        diffsq = difference ** 2
        total = total + diffsq

    sdev = math.sqrt(total / (len(alist) - 1))
    return sdev
