import time
import random

###########################################################
#   Selection Sort
#       - This algorithm will just go through the list
#       sequencially and sort the list in numeric order
#
#       - Parameters: List<int>
###########################################################
def selectionSort(numList):
    start_time = time.time()

    print(f"Starting Number List: {numList}")

    for i in range(len(numList)):
        min_index = i
        for j in range(i+1, len(numList)):
            if numList[min_index] > numList[j]:
                min_index = j

        numList[i], numList[min_index] = numList[min_index], numList[i]

    print(f"Selection sort executed in: {round(float(time.time() - start_time) * 1000, 2)} milliseconds")
    print(f"Sorted numList: {numList} \n\n")

###########################################################
#   Bubble Sort
#       - TBubble Sort is the simplest sorting algorithm 
#       that works by repeatedly swapping the adjacent 
#       elements if they are in wrong order
#
#       - Parameters: List<int>
###########################################################
def bubbleSort(numList):
    start_time = time.time()

    print(f"Starting Number List: {numList}")

    for i in range(len(numList) - 1):
        for j in range(0, len(numList) - i - 1):
            if numList[j] > numList[j + 1]:
                numList[j], numList[j + 1] = numList[j + 1], numList[j]

    print(f"Bubble sort executed in: {round(float(time.time() - start_time) * 1000, 2)} milliseconds")
    print(f"Sorted numList: {numList} \n\n")


###########################################################
#   Lucky Number Sorting Question
#       - A number is lucky if all digits of the number are 
#       different. How to check if a given number is lucky 
#       or not.
#
#       - Parameters: int
###########################################################
def luckyNumber(number):
    start_time = time.time()
    
    listOfDigits = [int(n) for n in str(number)]
    counter = 1;

    if len(listOfDigits) > 10:
        return "Sorry this number is too big to be deemed lucky"

    for i in range(len(listOfDigits) - 1):
        for j in range(0, len(listOfDigits) - i - 1):
            if listOfDigits[i] == listOfDigits[j + 1]:
                counter += 1
        
        if counter > 1:
            print(f"Selection sort executed in: {round(float(time.time() - start_time) * 1000, 2)} milliseconds")
            return f"False, {listOfDigits[i]} appears {counter} times"
        else:
            counter = 0
    
    print(f"Selection sort executed in: {round(float(time.time() - start_time) * 1000, 2)} milliseconds")
    return f"True, All digits are different and its your lucky day!"
                

#region Helper Functions

###########################################################
#   Create Large Int List
#       - This function is used to randomly generate a list
#       of integers between 1 and 100 with N length
#
#       - Parameters: int
###########################################################
def createLargeIntList(sizeOfList):
    intList = []
    for n in range(sizeOfList):
        intList.append(random.randint(1, 101))

    return intList

#endregion


if __name__ == "__main__":
    # numList = createLargeIntList(10)
    # selectionSort(numList)
    # numList = createLargeIntList(10)
    # bubbleSort(numList)
    print(luckyNumber(45656))