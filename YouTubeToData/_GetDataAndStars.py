import string
from itertools import islice

originalDict = dict()
newDict = dict()
nSplitter = 20

def chunks(data, SIZE=1000000):
    it = iter(data)
    for i in range(0, len(data), SIZE):
        yield {k: data[k] for k in islice(it, SIZE)}

def printDic(dictionary):
    for x in dictionary.keys():
        print(x)

# Copy the values of item into a dictionary we can use for ourselves
def copyOrgignalToNew(d, splitter):
    print('INSIDE LOOP')
    for item in chunks(d, splitter):
        # print('Name: ', list(item.keys())[0] ,item, 'sum is ', sum(item.values()))
        # Key would be the time it starts with the sum of the values between it
        newDict[list(item.keys())[0]] = sum(item.values())

def chunks(data, SIZE=1000000):
    it = iter(data)
    for i in range(0, len(data), SIZE):
        yield {k: data[k] for k in islice(it, SIZE)}



class CalculateData:
    def __init__(self, data_file_name, link_of_youtube_video, nameOfCommentFile):

        self.file = open(data_file_name) # Place filer we had into an instance variable
        # Have multiple data points to look for
        self.declareDics()  # Create the covers

        self.timeToDict() # Create the original

        improvedDicts = [
            self._10SplitDict,
            self._30SplitDict,
            self._50SplitDict,
            self._70SplitDict,
            self._90SplitDict,
            self._110SplitDict,
            self._130SplitDict,
            self._150SplitDict,
            self._170SplitDict,
            self._190SplitDict
        ]
        valuesForDicts = [
            10, 30, 50, 70, 90, 110, 130, 150, 170, 190
        ]

        # TODO BREAK HERE AT THIS METHOD

        # Make a for loop



        printDic(originalDict)

        copyOrgignalToNew(originalDict, nSplitter)

        starData = open('test.txt', 'w')
        # print(newDict)
        print('Old dict size: {}'.format(len(originalDict)))
        print('New dict size: {}'.format(len(newDict)))

        dic2 = dict(sorted(newDict.items(), key=lambda x: x[1]))
        starData.write("___HHMMSS\n")
        starData.write(("1st: {}\t*:{}\tHH:MM:SS\n".format(list(dic2)[-1], list(dic2.values())[-1])))
        starData.write(("2nd: {}\t*:{}\tHH:MM:SS\n".format(list(dic2)[-2], list(dic2.values())[-2])))
        starData.write(("3rd: {}\t*:{}\tHH:MM:SS\n".format(list(dic2)[-3], list(dic2.values())[-3])))
        starData.write(("4th: {}\t*:{}\tHH:MM:SS\n".format(list(dic2)[-4], list(dic2.values())[-4])))
        starData.write(("5th: {}\t*:{}\tHH:MM:SS\n".format(list(dic2)[-5], list(dic2.values())[-5])))
        starData.write(("6th: {}\t*:{}\tHH:MM:SS\n".format(list(dic2)[-6], list(dic2.values())[-6])))
        # starData.write(("7th: {}\t*:{}\tHH:MM:SS\n".format(list(dic2)[-7], list(dic2.values())[-7])))
        # starData.write(("8th: {}\t*:{}\tHH:MM:SS\n".format(list(dic2)[-8], list(dic2.values())[-8])))
        # starData.write(("9th: {}\t*:{}\tHH:MM:SS\n".format(list(dic2)[-9], list(dic2.values())[-9])))
        # starData.write(("10th: {}\t*:{}\tHH:MM:SS\n".format(list(dic2)[-10], list(dic2.values())[-10])))
        sumOfData = sum(dic2.values())
        numOfData = len(dic2)
        avg = (sumOfData / numOfData) + nSplitter
        starData.write("Avg: {}\n".format(avg))
        starData.write('\n')

        # Write to the text file stars :: Perhaps didive by 10 or something to lower it's meaning 270 -> 27 stars
        for x, y in newDict.items():
            # print(x,":",y)
            # print('Start at',x,'\t', end ="")
            starData.write(("Start at {} *:{}\t".format(x, y)))
            for n in range(y):
                starData.write(('*'))
            # print("*", end ="")
            # print()
            starData.write("\n")

        print('LOOK AT ME!!!')



    # Places the data into a dictionary for us to use
    def timeToDict(self):
        # Loop through each line of the file
        for line in self.file:
            # Remove the leading spaces and newline character
            line = line.strip()

            # Convert the characters in line to
            # lowercase to avoid case mismatch
            line = line.lower()

            # Remove the punctuation marks from the line
            # line = line.translate(line.maketrans("", "", string.punctuation)) # This removes the ':'

            # Split the line into words
            words = line.split(" ")
            # Iterate over each word in line
            for word in words:
                # Looks for a negative value and skips it
                if (check_negative_sign(word)):
                    pass
                # Check if the word is already in dictionary
                elif word in originalDict:
                    # Increment count of word by 1
                    originalDict[word] = originalDict[word] + 1
                else:
                    # Add the word to dictionary with count 1
                    originalDict[word] = 1


    def printDic(self, dictionary):
        for x in dictionary.keys():
            print(x)

    def chunks(self, data, SIZE=1000000):
        it = iter(data)
        for i in range(0, len(data), SIZE):
            yield {k: data[k] for k in islice(it, SIZE)}


    def declareDics(self):
        self.originalDict = dict()
        self._10SplitDict = dict()
        self._30SplitDict = dict()
        self._50SplitDict = dict()
        self._70SplitDict = dict()
        self._90SplitDict = dict()
        self._110SplitDict = dict()
        self._130SplitDict = dict()
        self._150SplitDict = dict()
        self._170SplitDict = dict()
        self._190SplitDict = dict()


# Looks to see of the first character is a negative sign
def check_negative_sign(s):
    if(s[0] == '-'):
        return True
    else:
        return False

