# Game 1: 1 green, 4 blue; 1 blue, 2 green, 1 red; 1 red, 1 green, 2 blue; 1 green, 1 red; 1 green; 1 green, 1 blue, 1 red


class InputParser:
    '''Parses a text input into readablie dictionaries'''
    RED = 12
    GREEN = 13
    BLUE = 14
    def __init__(self, file_name:str):
        self.file_name = file_name
        self.color_limits:dict[str:int] = {"red": self.RED, "green": self.GREEN, "blue": self.BLUE}

    def get_input(self):
        with open(self.file_name, 'r') as file:
            lines = [line.rstrip() for line in file]
            return lines
        
    def get_game_number(self, line:str)->int:
        game_info = line.split(": ")[0]
        game_number = game_info.split(" ")[1]
        return int(game_number)
    
    def get_game_rounds(self,line:str)->list[str]:
        game = line.split(": ")[1]
        game_rounds = game.split("; ")
        return game_rounds
    
    def get_min_colours(self, game_rounds:list[str])->dict[str:int]:
        '''Outputs the maximum value of each colour into a dictionary'''
        min_colours:dict[str:int] = {"red": 0, "green": 0, "blue": 0}
        for game_round in game_rounds:
            colour_list = game_round.split(", ") #output eg [1 green, 2 blue]
            # print(f"{game_round=}")
            for colour in colour_list:
                [colour_count,colour_name]  = colour.split(" ") # output eg [1, green]
                # print(f"{colour_count=}, {colour_name=}")
                obj = object()
                # print(f"{min_colours.get(colour_name, obj)=}")
                if min_colours.get(colour_name, obj) != obj and int(colour_count) > min_colours[colour_name]:
                    min_colours[colour_name] = int(colour_count)

        return min_colours
    

    def is_game_valid(self, line:str)->bool:
        '''Checks if the game is valid'''
        game_rounds = self.get_game_rounds(line)
        max_colours = self.get_min_colours(game_rounds)
        for colour in max_colours:
            if max_colours[colour] > self.color_limits[colour]:
                return False
        return True

    def get_valid_games_sum(self, lines:list[str])->int:
        '''Returns the sum of all valid game numbers'''
        valid_games_sum = 0
        for line in lines:
            print(self.get_game_number(line), self.get_min_colours(self.get_game_rounds(line)))
            if self.is_game_valid(line):
                valid_games_sum += self.get_game_number(line)
        return valid_games_sum
    
    def get_game_power(self,line:str)->int:
        game_rounds = self.get_game_rounds(line)
        min_colours = self.get_min_colours(game_rounds)
        power = 1
        for colour in min_colours:
            power *= min_colours[colour]
        return power
    
    def get_overall_power(self, lines:list[str])->int:
        '''Returns the sum of all game powers'''
        overall_power = 0
        for line in lines:
            overall_power += self.get_game_power(line)
        return overall_power

if __name__ == "__main__":
    parser = InputParser("input.txt")
    lines = parser.get_input()

    print(parser.get_overall_power(lines))

        
    