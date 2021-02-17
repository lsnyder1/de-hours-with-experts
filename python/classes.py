class NumberObj(object):
    """docstring for ."""

    def __init__(self, number):
        #building all properties to consider on init
        self.numberStr = number
        #removing "-" and "." if present We will reinsert later if present, but will rely on properties as flags
        self.processedInputStr=''.join([k for k in self.numberStr if k not in ["-","."]])
        #we only care about the processed string length for our purposes
        self.processedInputLength=len(self.processedInputStr)
        #flags for manipulating string at end, validating string as input is assumed sanitized
        self.isNegative=True if "-" in self.numberStr else False
        self.isFloat=True if "." in self.numberStr else False






    def getNextBiggest(self):
        #cast the string to int list
        numberList=[int(x) for x in self.processedInputStr]
        #just here for something to insert "-" and"." , then return "".join later
        finishedStrList=[]
        #holds all of the numbers we will remove from numberList, we will have to reorganize these to build correct number
        tempList=[]
        #max index for numberList to use as start for while loop counter to work from right ot left
        i=-1
        if self.processedInputLength>1:
            i=self.processedInputLength-1

        while i > -1:
            #print(f"numList: {numberList}")
            #Break from the while loop by returning as soon as there is a value higher than the last remaining index of numberList, or lower if negative
            #hold this value because we are going to remove it from numberList and need to compare in loop below
            tempVal=numberList[i]
            #moving values between lists to indicate
            tempList.append(tempVal)
            tempList.sort()
            del numberList[i]

            #testLogs to be removed
            #print(f"tempVal: {tempVal}")
            #print(f"maxTempList: {max(tempList)}")
            #print(f"TempList: {tempList}")

            #if this evaulates to true we are done looping, time to build the return string
            if(max(tempList)>tempVal and not self.isNegative) or (min(tempList)<tempVal and self.isNegative):
                if self.isNegative==False:
                #positive numbers

                    biggerThanIList=[x for x in tempList if x>tempVal]
                    biggerThanIList.sort()
                    #put the lowest value back in numberList
                    numberList.append(biggerThanIList[0])
                    #remove this number from tempList, don't care if more than one instance as long as we remove one
                    tempList.remove(biggerThanIList[0])
                    #sort to ensure ascending order
                    tempList.sort()

                else:
                #negative numbers

                    smallerThanIList=[x for x in tempList if x<tempVal]
                    smallerThanIList.sort(reverse=True)
                    numberList.append(smallerThanIList[0])
                    tempList.remove(smallerThanIList[0])
                    tempList.sort(reverse=True)
                    finishedStrList.insert(0,"-")

                #+=here since we already have [0] if negative
                finishedStrList+=[str(y) for y in numberList+tempList]
                if self.isFloat:
                    finishedStrList.insert(self.numberStr.index("."),".")
                return "".join(finishedStrList)

            #decrementing as working right to left through user numberList
            i-=1
            #if we ever get here, no higher number was possible
        return -1


#Debug method to return all Object properties
    def dump(self):
        temp=""
        for attr in dir(self):
            temp+=("self.%s = %r" % (attr, getattr(self, attr)))
        return temp
