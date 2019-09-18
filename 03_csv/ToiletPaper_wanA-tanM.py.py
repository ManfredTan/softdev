#Albert Wan and Manfred Tan
#SoftDev1 pd9
#K06 -- Divine your Destiny!
#2019-09-17


import random
import csv

newDict = {}

def createDict(csvFile):

    # we use "with...as" because it automatically closes file after
    # it finishes, which makes our life easier.
    # open returns a file object, which is an iterator and iterable
    with open(csvFile, "r") as oldcsv:
        csvRead = csv.reader(oldcsv) # standard delimiter is ","
        next(csvRead) # skips first line
        for row in csvRead:
            newDict[(row[0])] = float(row[1]) # adds data into dictionary
    del newDict["Total"] # remove total percentage (final line)
    return newDict


def createArray(dict):
    # puts occupations and percentages of each occupation into separate lists.
    # dictOccupations.keys() and .values() return dict-key object and dict-value
    # objects respectively, so we need to convert to list
    occupationList = list( dict.keys() )
    percentageList = list( dict.values() )

    # chooses random float from 0.0 to 100.0, not including 100.0
    randomNumber = random.random() * 100

    # each percent has a "range". For example, 0-6.1 is management and
    # 6.1 -11.1 is business and finance. Management takes up 6.1/100 spots,
    # while business takes up 5/100 spots. If the random number falls in that range,
    # that occupation is picked.
    currentPercent = 0.0
    index = 0
    while index < len(percentageList):
        currentPercent += percentageList[index]
        if randomNumber < currentPercent:
            print("Random Occupation: " + occupationList[index])
            print("Workforce Percentage: " + str( percentageList[index]) )
            return
        index += 1

createArray(createDict('occupations.csv'))
