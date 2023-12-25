def contains_number(string, reversed=False):
    """
    Returns the number of the string if it contains a number, else returns None
    """

    if reversed:
        numbers = ["eno", "owt", "eerht", "ruof", "evif", "xis", "neves", "thgie", "enin"]
    else:
        numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    numbers_int = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
    for i, char in enumerate(string):
        ## If the char is a number, return the number
        if char in numbers_int:
            return int(char)
        
        ## If the char is a letter, check if the next chars makes up a number
        if len(string) > i + 2:
            num = string[i:i+3]
            if num in numbers:
                return numbers.index(num) + 1
        if len(string) > i + 3:
            num = string[i:i+4]
            if num in numbers:
                return numbers.index(num) + 1
        if len(string) > i + 4:
            num = string[i:i+5]
            if num in numbers:
                return numbers.index(num) + 1

if __name__ == "__main__":
    ## Read file from input.txt
    with open("input.txt", "r") as f:
        input = f.read()
    
    ## Split input into list of strings
    input = input.split("\n")

    sum = 0
    for string in input:
        number = int(str(contains_number(string)) + str(contains_number(string[::-1], True)))
        print(number)
        sum += number
    print(sum)
    