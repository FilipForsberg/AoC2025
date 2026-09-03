"""
Batteries are arranged into banks -> 1 line of input
Each battery has a value from 1 to 9 ie a Bank can look like 123456789, where battery 1 has value 1 etc. 


Need to turn on exactly 2 batteries within each bank!
The total voltage the bank will create is the concatination of the battery values. So if i turn on battery 1 and 9 in previous example i get 19. Can do that as str(1) + str(9)
Need to find the largest possible value within each bank, BUT can not change the order. So for the 123456789 example the biggest possible is 89

Find the total voltage across all banks.

So for each bank: Find the largest number from range(0, len(line)) (Do not include last value as we need atleast 2 values)
Then go through the line again from (pos(max) - len(line+1)) and find the next biggest


This can also be done for part2 where we need to find 12. However should be able to do more nicely, maybe using lists nad using pops/append

pop() optional index, if none given defaults to -1, and removes + returns the item at that index.
"""

def find_largest(s:str,  includeLast: bool = False, startIndex:int = 0) -> tuple[str, int]:
    largest = '0'
    largest_index = -1
    if (includeLast):
        end_index = len(s)
    else:
        end_index = len(s) - 1


    #print("Start index: " , startIndex , ";  End index: " , end_index)
    for i, ch in enumerate(s[startIndex:end_index], start=startIndex):
        if ch > largest:
            largest = ch
            largest_index = i
    return largest, largest_index


def solve_p1(data):
    counter = 0

    for line in data:
        firstValue, index = find_largest(line)
        #print("FirstValue: " , firstValue , "  ; Index " , index)
        secondValue, secondIndex = find_largest(line, includeLast=True, startIndex=index+1)
        #print("Secondvalue: " , secondValue , "  ; Second index: " , secondIndex)
        #print("Adding: ", int(firstValue + secondValue))
        counter += int(firstValue + secondValue)
        

    return counter

def solve_p2(data):
    counter = 0
    for line in data:
        counter += int(find_largest_n(line, 12))
    return counter

def find_largest_n(s:str, n:int) -> str:

    to_remove = len(s) - n
    stack = []
    print(s, to_remove)
    for i,ch in enumerate(s):
        while to_remove > 0 and stack and stack[-1] < ch:
            stack.pop()
            to_remove -= 1
        stack.append(ch)

    stack = stack[:n]
    digits = "".join(ch for ch in stack)
    print(digits)
    return digits



def load_data(dir):
    with open(dir, "r") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    return lines

if __name__ == "__main__":

    test_data = load_data("test.txt")
    input_data = load_data("input.txt")
    
    # P1 17281
    print("P1 test data: " ,solve_p1(test_data))
    print("P1 input data: " ,solve_p1(input_data))

    #P2 171388730430281
    print("P2 test data: " ,solve_p2(test_data))
    print("P2 input data: " ,solve_p2(input_data))