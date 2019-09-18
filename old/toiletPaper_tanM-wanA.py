# Manfred Tan and Albert Wan
# SoftDev1 pd9
# K#06 - CSV Reader
# 2019-09-17


# to access csv commands!
import csv, random

# making dictionary for occupations
dictOccupations = {}

def makeDictOccupations(filename):

    # we use "with...as" because it automatically closes file after
    # it finishes, which makes our life easier.
    # open returns a file object, which is an iterator and iterable
    with open( filename, 'r') as entire_file:

        # makes a list, where each row is a string in the list
        data = entire_file.readlines()

    # removes first string
    data.pop(0)

    # takes last string, splits into list using comma,
    # takes element 1 of list, turns it from string to float. whew
    totalPercent = float(data[-1].split(",")[1])

    # removes last string
    data.pop(-1)

    # csv.reader method takes in an iterable and returns a reader object.
    # The __next__() method in the reader object returns the
    # next row of the reader's iterable oject as a list.
    # i.e, for each row it returns a list of strings (in this case).
    data_as_lists = csv.reader(data)

    # adding each data point into the dictionary
    for row_as_list in data_as_lists:
        dictOccupations.update({ row_as_list[0]:row_as_list[1] })

    #print(dictOccupations)


def randomOccupation():

    # puts occupations and percentages of each occupation into separate lists.
    # dictOccupations.keys() and .values() return dict-key object and dict-value
    # objects respectively, so we need to convert to list
    occupationList = list( dictOccupations.keys() )
    percentageList = list( dictOccupations.values() )

    # chooses random float from 0.0 to 100.0, not including 100.0
    randomNumber = random.random() * 100

    # each percent has a "range". For example, 0-6.1 is management and
    # 6.1 -11.1 is business and finance. Management takes up 6.1/100 spots,
    # while business takes up 5/100 spots. If the random number falls in that range,
    # that occupation is picked.
    currentPercent = 0.0
    index = 0
    while index < len(percentageList):
        currentPercent += float( percentageList[index] )
        if randomNumber < currentPercent:
            print("Random Occupation: " + occupationList[index])
            print("Workforce Percentage: " + percentageList[index])
            return
        index += 1



makeDictOccupations("occupations.csv")
randomOccupation()



# ***NOTES***

# sequence = generic term for ordered set.

# iterable object is something that can be iterated upon. ex: lists, strings

# iterator object allows us to access elements in container one at a time.
# iterator object has a next() method, which helps us access each element.
# this object remembers where it is / at which element it is at.
# every iterator is always an iterable, not always for vice versa

# delimiter = what separates data. Usually ","
