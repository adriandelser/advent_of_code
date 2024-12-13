from typing import Generator
import numpy as np

class InputParser:
    def __init__(self, file_name:str):
        self.file_name = file_name
        #pad input for window
        self.lines = self.get_input()
        # self.lines = self.lines_padded[1:-1]

    def get_input(self):
        with open(self.file_name, 'r') as file:
            lines = ["."+line.rstrip()+"." for line in file]
            lines.insert(0,"."*(len(lines[0])))
            lines.append("."*(len(lines[0])))
            return lines
        
    def number_generator(line:str)->Generator[tuple[int,int],None,None]:
        """Creates a generator object that yields the next number in the string

        Args:
            line (str): line of text from the input

        Yields:
            Generator[tuple[int, int],None,None]: yields Int, does not expect to receive any values or return any value upon completion
        """
        number = ''
        for index, char in enumerate(line):
            if char.isdigit():
                if number == '':
                    start_index = index
                number += char
            elif number:
                yield (start_index,int(number))
                number = ''
        if number:
            yield (start_index,int(number))

    def get_lookup_array(self,index:int, number:int, line_index:int)->list:
        "checks if number is valid"
        n = len(str(number))
        lookup_array = np.array([[*line[index-1:index+n+1]] for line in self.lines[line_index-1:line_index+2]])
        return lookup_array
    
    def is_valid_array(self,array:list)->bool:
        "checks if number is valid"
        # Convert array elements to string, check if they are digits or '.', and use np.logical_not
        return np.any(np.logical_not(np.char.isdigit(array) | (array == '.')))


if __name__ == '__main__':
    input_parser = InputParser('input.txt')
    s = 0
    for line_idx, line in enumerate(input_parser.lines):
    # line = input_parser.lines[1]
        number_generator = InputParser.number_generator(line)
        for idx, number in number_generator:
            # print(idx,number)
            a = input_parser.get_lookup_array(idx,number,line_idx)
            if input_parser.is_valid_array(a):
                s += number
    print(s)