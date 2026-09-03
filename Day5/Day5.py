"""
Input will look like:
List of ranges for ID that are deemed FRESH
A blank line
Followed by list of available ingredients. 

Ie:
3-5
10-14
16-20
12-18

1
5
8
11
17
32


The ranges are INCLUSIVE

P1: Want to find how many ingredients are fresh given the list of ranges and list of ingredients. 
P2: Find how many valid ids are inside the ranges. Ranges can overlap however so need to find the overlap and create potentially bigger combined range to avoid double counting.
"""

def load_data(dir):
    with open(dir, "r") as f:
        lines = f.read()
    ranges_block, values_block = lines.strip().split("\n\n")
    ranges = ranges_block.splitlines()
    values = values_block.splitlines()
    return ranges, values

def parse_range(s:str) -> range:
    start, end = s.split("-")
    return range(int(start), int(end) + 1)

def solve_p1(ranges, values):
    num_ranges = [parse_range(range) for range in ranges]
    counter = 0
    for value in values:
        if any(int(value) in r for r in num_ranges):
            counter += 1

    return counter

def solve_p2(ranges):
    num_ranges = sorted((r.start, r.stop) for r in (parse_range(range) for range in ranges))

    total = 0


    """
    If the ranges overlap, update the current end to match the new biggest range. 
    If they dont overlap, get the total number of ids in the range and move to the next one
    """
    current_start, current_end = num_ranges[0]
    for start, end in num_ranges[1:]:
        if start <= current_end:
            current_end = max(current_end, end)
        else: 
            total += current_end - current_start
            current_start, current_end = start, end
    total += current_end - current_start
    return total

if __name__ == "__main__":

    #input_data = load_data("input.txt")
    t_ranges, t_values = load_data("test.txt")
    print("P1 test: ", solve_p1(t_ranges, t_values))
    i_ranges, i_values = load_data("input.txt")
    print("P1 input: ", solve_p1(i_ranges, i_values))

    print("P2 test ", solve_p2(t_ranges))
    print("P2 input ", solve_p2(i_ranges))