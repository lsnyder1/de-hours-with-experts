class NumberObj(object):
    """docstring for ."""

    def __init__(self, number):
        #building all properties to consider on init
        self.numberStr = number
        #removing "-" and "." if present We will reinsert later if present, but will rely on other flags at that time
        self.processedInputStr=''.join(filter(lambda k: k not in ["-","."], self.numberStr))
        #we only care about the processed string length for our purposes
        self.processedInputLength=len(self.processedInputStr)
        #flags for manipulating string at end, validating string as input is assumed sanitized
        self.isNegative=True if "-" in self.numberStr else False
        self.isFloat=True if "." in self.numberStr else False
        if self.isFloat:
            #declaring here so self.decimalIndex is none/null if not isFloat we're going to insert back in later if isFloat immediately after "-" if needed so our index is valid
            self.decimalIndex=self.numberStr.index(".")




    def getNextBiggestPos(self):
        #cast the string to int list
        numberList=list(map(lambda x:int(x),self.processedInputStr))
        #just here for something to insert "-" and"." , then return .join later
        finishedStrList=[]
        #holds all of the numbers we will removed from numberList, we will have to reorganize these to build correct number
        tempList=[]
        #max index for numberList to use as start for while loop counter to work from right ot left
        i=len(numberList)-1


        while i > -1:
            #Break from the while loop as soon as there is a value higher than the last remaining index of numberList
            #hold this value because we are going to remove it from numberList and need to compare in loop below
            tempVal=int(numberList[i])

            tempList.append(tempVal)
            tempList.sort()
            numberList.pop(i)

            if max(tempList)>tempVal:
                #need to grab all values bigger than the one we just cut so we can select the smallest one as a replacement
                biggerThanIList=list(filter(lambda x:x>tempVal,tempList))

            #decrementing as working right to left in List
            i-=1
            #if int(numberList[i-1])<int(numberList[i]):
        return biggerThanIList
        #return finishedNum.join(tempList)
        #return finishedNum.join(numberList)
        #return count

    def nextBiggestNeg(self):
        return

#Debug method to return all Object properties
    def dump(self):
        temp=""
        for attr in dir(self):
            temp+=("self.%s = %r" % (attr, getattr(self, attr)))
        return temp
