import re

def load_data(dir):
    with open(dir, "r") as f:
        ranges = f.read()
        ranges = ranges.split(",")
    return ranges


def parse_range(s:str) -> range:
    start, end = s.split("-")
    return range(int(start), int(end) + 1)


def is_valid(i:int) -> bool:
    s = str(i)
    s_len = len(s)

    if (s_len % 2 == 1):
        return True
    mid_point = s_len // 2
    return s[:mid_point] != s[mid_point:]

def solve_p1(data):
    counter = 0
    ranges = [parse_range(r) for r in data]

    for r in ranges:
        counter += sum(i for i in r if not is_valid(i))
    return counter

def solve_p2(data):
    """
    Invalid if repeated ATLEAST twice. 
    Need to check if EACH sublength matches 
    Can do similiar to p1 but would need ot check each possible sublength between 1 and len(string) // 2
    Should be possible with regex. 
    Which should be all we need. 
    """
    counter = 0
    ranges = [parse_range(r) for r in data]
    for r in ranges:
        counter += sum(i for i in r if not is_valid_regex(i))
    return counter
    
def is_valid_regex(num:int) -> bool:
    """    
    r treat string as raw
        Regex meta characters
        ^ starts with
        $ ends with
        () creates a group
        + one or more occurrnces
        \ signals a special sequence, for example \d to returns match where string contains digits. 
        \1 look at the first created group
    """
    return not re.match(r"^(\d+)\1+$", str(num))


if __name__ == "__main__":

    test_data = load_data("test.txt")
    input_data = load_data("input.txt")

    print("P1 - Test data: " ,solve_p1(test_data))
    print("P1 - Real Data: ", solve_p1(input_data))

    print("P2 - Test data: " ,solve_p2(test_data))
    print("P2 - Real Data: ", solve_p2(input_data))