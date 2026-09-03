def solve(inputs, part = 1):
    start_point = 50
    zero_count = 0

    for operation in inputs:
        start_point, turns = rotate(operation[0], operation[1], start_point)
        if part == 2:
            zero_count += turns
        if (start_point == 0):
            zero_count += 1
    return zero_count
    
def construct_data_array(dir):
    inputs = []
    with open(dir, "r") as f:
            for line in f:
                line = line.strip()
                direction = line[0]
                value = (int)(line[1:])
                inputs.append((direction,value))
    return inputs
        

def rotate(direction, value, start_value):
    if (direction == "R"):
        turns, new_value = divmod(start_value+value, 100)
        if new_value == 0:
            turns -= 1
    elif(direction == "L"):
        turns, new_value, = divmod(start_value-value, 100)

        if (start_value == 0):
            turns += 1
    return new_value, abs(turns)


if __name__ == "__main__":

    input_data = construct_data_array("input/p1_input.txt")
    test_data = construct_data_array("input/test.txt")
    #1165
    sum = solve(input_data)
    print(sum)

    #6496
    sum2 = solve(input_data, part=2)
    print(sum2)