from math import pow


class Noughts_And_Crosses:
    def __init__(self, arena_size, in_rows_to_win):
        self.arena_size = arena_size
        self.in_rows_to_win = in_rows_to_win
        self.arena = []
        self.symbols = ['x', 'o']
        self.rounds_played = 0
        self.arena_slots = int(pow(arena_size, 2))
        self.players_list = []

    def create_arena(self):
        x_axle = []

        for i in range(self.arena_size):
            for i in range(self.arena_size):
                x_axle.append(' ')
            self.arena.append(list(x_axle.copy()))
            x_axle.clear()

    def get_slots(self):
        return self.arena_slots
    
    def get_in_rows_to_win(self):
        return self.in_rows_to_win
    
    def get_symbol(self, player):
        return self.symbols[player]
    
    def get_symbol_list(self):
        return self.symbols

    def nice_print(self):
        top_info_row = ""
        for i in range(self.arena_size+1):
            top_info_row += f'{i} '
        print(top_info_row)

        for i in range(self.arena_size):
            temp_string = ' '.join(self.arena[i])
            print(f'{i+1} {temp_string}')
    
    def add_round(self):
        self.rounds_played += 1
    
    def get_rounds_played(self):
        return self.rounds_played

    def players_to_list(self, player_x, player_o):
        self.players_list = [player_x, player_o]
        
    def try_input(self):
        while True:
            try:
                temp_input = int(input())
            except ValueError:
                print("Value os not an interger, try again")
                continue
       
            if(1 <= temp_input <= self.arena_size + 1):
                temp_input -= 1
                return temp_input
                break
            else:
                print("Cordinate outside arena, try again")

    def empty_slot_test(self, y, x):
        if(self.arena[y][x] == ' '):

            return True
        else:
            print("Slot already taken, try again.")
            return False
    
    def save_play(self, y, x, player):
        player = self.symbols[player]
        self.arena[y][x] = player

    def search_right(self, y, x, player):
        right = x+(self.in_rows_to_win)
        if(0 <= right <= self.arena_size):
            in_row_counter = 0
            for i in range(0, self.in_rows_to_win):
                if(self.arena[y][x+i] == self.symbols[player]):
                    in_row_counter += 1
            return in_row_counter
        return 0

    def search_left(self, y, x, player):
        left = x-(self.in_rows_to_win-1)
        if(0 <= left <= self.arena_size):
            in_row_counter = 0
            for i in range(0, self.in_rows_to_win):
                if(self.arena[y][x-i] == self.symbols[player]):
                    in_row_counter += 1
            return in_row_counter
        return 0
    
    def search_down(self, y, x, player):
        down = y+(self.in_rows_to_win)
        if(0 <= down <= self.arena_size):
            in_row_counter = 0
            for i in range(0, self.in_rows_to_win):
                if(self.arena[y+i][x] == self.symbols[player]):
                    in_row_counter += 1
            return in_row_counter
        return 0
    
    def search_up(self, y, x, player):
        up = y-(self.in_rows_to_win-1)
        if(0 <= up <= self.arena_size):
            in_row_counter = 0
            for i in range(0, self.in_rows_to_win):
                if(self.arena[y-i][x] == self.symbols[player]):
                    in_row_counter += 1
            return in_row_counter
        return 0

    def search_down_right(self, y, x, player):
        down = y+(self.in_rows_to_win)
        if(0 <= down <= self.arena_size):
            right = x+(self.in_rows_to_win)
            if(0 <= right <= self.arena_size):
                in_row_counter = 0
                for i in range(0, self.in_rows_to_win):
                    if(self.arena[y+i][x+i] == self.symbols[player]):
                        in_row_counter += 1
                return in_row_counter
        return 0
    
    def search_down_left(self, y, x, player):
        down = y+(self.in_rows_to_win)
        if(0 <= down <= self.arena_size):
            left = x-(self.in_rows_to_win-1)
            if(0 <= left <= self.arena_size):
                in_row_counter = 0
                for i in range(0, self.in_rows_to_win):
                    if(self.arena[y+i][x-i] == self.symbols[player]):
                        in_row_counter += 1
                return in_row_counter
        return 0
    
    def search_up_right(self, y, x, player):
        up = y-(self.in_rows_to_win-1)
        if(0 <= up <= self.arena_size):
            right = x+(self.in_rows_to_win)
            if(0 <= right <= self.arena_size):
                in_row_counter = 0
                for i in range(0, self.in_rows_to_win):
                    if(self.arena[y-i][x+i] == self.symbols[player]):
                        in_row_counter += 1
                return in_row_counter
        return 0

    def search_up_left(self, y, x, player):
        up = y-(self.in_rows_to_win)
        if(0 <= up <= self.arena_size):
            right = x+(self.in_rows_to_win)
            if(0 <= right <= self.arena_size):
                in_row_counter = 0
                for i in range(0, self.in_rows_to_win):
                    if(self.arena[y-i][x-i] == self.symbols[player]):
                        in_row_counter += 1
                return in_row_counter
        return 0


class Players:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)


player1 = Players("Joe")
player2 = Players("Jeff")

match = Noughts_And_Crosses(3, 3)
match.create_arena()

match.players_to_list(player1, player2)
'''
match.save_play(0, 0, 0)
match.save_play(0, 1, 0)
match.save_play(0, 2, 0)
'''


match.nice_print()
symb_list = ['x', 'o']
keep_loop = True

while(keep_loop is True):
    for player in range(0, 2):
        print(f'Player \"{symb_list[player]}\", enter cordinate X')
        x_cord = match.try_input()
    
        print(f'Player \"{symb_list[player]}\", enter cordinate Y')
        y_cord = match.try_input()

        if(match.empty_slot_test(y_cord, x_cord) is True):
            match.save_play(y_cord, x_cord, player)
            match.nice_print()
            match.add_round()
            if(match.search_left(y_cord, x_cord, player) == match.get_in_rows_to_win()):
                keep_loop = False
                print(f'Winner: player \"{match.get_symbol(player)}\"')
                break
            if(match.search_right(y_cord, x_cord, player) == match.get_in_rows_to_win()):
                keep_loop = False
                print(f'Winner: player \"{match.get_symbol(player)}\"')
                break
            if(match.search_down(y_cord, x_cord, player) == match.get_in_rows_to_win()):
                keep_loop = False
                print(f'Winner: player \"{match.get_symbol(player)}\"')
                break
            if(match.search_up(y_cord, x_cord, player) == match.get_in_rows_to_win()):
                keep_loop = False
                print(f'Winner: player \"{match.get_symbol(player)}\"')
                break
            if(match.search_down_right(y_cord, x_cord, player) == match.get_in_rows_to_win()):
                keep_loop = False
                print(f'Winner: player \"{match.get_symbol(player)}\"')
                break
            if(match.search_down_left(y_cord, x_cord, player) == match.get_in_rows_to_win()):
                keep_loop = False
                print(f'Winner: player \"{match.get_symbol(player)}\"')
                break
            if(match.search_up_right(y_cord, x_cord, player) == match.get_in_rows_to_win()):
                keep_loop = False
                print(f'Winner: player \"{match.get_symbol(player)}\"')
                break
            if(match.search_up_left(y_cord, x_cord, player) == match.get_in_rows_to_win()):
                keep_loop = False
                print(f'Winner: player \"{match.get_symbol(player)}\"')
                break
    
        if(match.get_slots == match.get_rounds_played()):
            print("Draw")
            keep_loop = False
            break