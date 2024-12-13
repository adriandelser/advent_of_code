import sys

with open("input.txt") as f:
    lines = f.readlines()

#dictionary converting the words one through nine to their integer values
word_to_int:dict[str,int]  = {
    "zero":0,
    "one":1,
    "two":2,
    "three":3,
    "four":4,
    "five":5,
    "six":6,
    "seven":7,
    "eight":8,
    "nine":9}

#function to check if a any key in a dictionary is a substring of an input string 
#also returns where the key is in the input string
#returns None if no key is a substring of the input string

def substring_value(input_str: str, dict: dict) -> tuple|None:
    for key, value in dict.items():
        index = input_str.find(key)
        if index != -1:
            return key, value, index
    return (None,None,None)

# print(substring_value("arfiveighta2",word_to_int))

# print("arfiveighta2"[3:])
# print(lines[:5])


sum = 0 
for line in lines[:]:
    # print(line)
    digits:list[str] = []
    buffer:str = ""
    for char in line:
        if char.isnumeric():
            digits.append(char)
            # print(f"{digits=}")
        elif char.isalpha():
            buffer+=char
        # print(buffer)
        key,value,index = substring_value(buffer, word_to_int)
        if value is not None:
            digits.append(str(value))
            # print(f"{digits=}")
            buffer = buffer[index+1:]
    code:int = int(digits[0]+digits[-1])
    # print(code)
    # print(code)
    # print(code)
    sum+=code
print(sum)

# print(any("alpha" in ["balpha","dras"]))



