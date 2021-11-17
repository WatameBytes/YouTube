import string
from itertools import islice

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


        # Make a for loop
        for x in range(len(improvedDicts)):
            self.copyOrgignalToNew(self, improvedDicts[x], valuesForDicts[x])

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
                if (check_negative_sign(word)):
                    pass
                # Check if the word is already in dictionary
                elif word in self.originalDict:
                    # Increment count of word by 1
                    self.originalDict[word] = self.originalDict[word] + 1
                else:
                    # Add the word to dictionary with count 1
                    self.originalDict[word] = 1


    def printDic(self, dictionary):
        for x in dictionary.keys():
            print(x)



    # Copy the values of item into a dictionary we can use for ourselves
    def copyOrgignalToNew(self, dictionary, splitter):
        print('INSIDE LOOP')
        for item in self.chunks(dictionary, splitter):
            # print('Name: ', list(item.keys())[0] ,item, 'sum is ', sum(item.values()))
            # Key would be the time it starts with the sum of the values between it
            dictionary[list(item.keys())[0]] = sum(item.values())

    def chunks(data, SIZE=1000000):
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

