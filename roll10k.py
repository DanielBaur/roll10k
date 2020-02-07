# This script is meant to provide a framework for playing (and statistically analyzing) the dice game 'Bis 10.000 Würfeln'.



import numpy as np
import random





lut_dict = {
    "ones" : {
        "0" : [0],
        "1" : [100],
        "2" : [200],
        "3" : [1_000],
        "4" : [10_000],
        "5" : [100_000],
        "6" : [1_000_000]    
    },
    "twos" : {
        "0" : [0],
        "1" : [0],
        "2" : [0],
        "3" : [200],
        "4" : [2_000],
        "5" : [20_000],
        "6" : [200_000]    
    },
    "threes" : {
        "0" : [0],
        "1" : [0],
        "2" : [0],
        "3" : [300],
        "4" : [3_000],
        "5" : [30_000],
        "6" : [300_000]    
    },
    "fours" :{
        "0" : [0],
        "1" : [0],
        "2" : [0],
        "3" : [400],
        "4" : [4_000],
        "5" : [40_000],
        "6" : [400_000]    
    },
    "fives" : {
        "0" : [0],
        "1" : [0],
        "2" : [0],
        "3" : [500],
        "4" : [5_000],
        "5" : [50_000],
        "6" : [500_000]    
    },
    "sixes" : {
        "0" : [0],
        "1" : [0],
        "2" : [100],
        "3" : [600],
        "4" : [6_000],
        "5" : [60_000],
        "6" : [600_000]    
    },
    "special" : {
        "straight" : [1_000, 6, [1,1,1,1,1,1,]]
    }
}





class turn:
    
    def __init__(self):
        self.points = 0
        self.dice_available = 6
        self.rolls_list = []
        self.output_list = []
        self.can_go_on = True
        self.current_rolls = {
            "ones" : 0,
            "twos" : 0,
            "threes" : 0,
            "fours" : 0,
            "fives" : 0,
            "sixes" : 0,
        }

    def new_dice_roll(self, nod=dice_available):
        self.roll_set = list([random.randrange(1,7) for i in range(nod)])
        self.current_rolls["ones"] = self.roll_set.count(1)
        self.current_rolls["twos"] = self.roll_set.count(2)
        self.current_rolls["threes"] = self.roll_set.count(3)
        self.current_rolls["fours"] = self.roll_set.count(4)
        self.current_rolls["fives"] = self.roll_set.count(5)
        self.current_rolls["sixes"] = self.roll_set.count(6)
        self.rolls_list.append(self.current_rolls)

    def show_current_roll(self):
        print("######################################################")
        print(f"roll {len(self.rolls_list)}:")
        print("######################################################")
        for key, val in self.rolls_list[len(self.rolls_list)-1].items():
            print(f"{key}:\t {val}")
        print("######################################################")

    def reset_game(self):
        self.points = 0

    def evaluate_current_dice_roll(self, mode="daniel"):
        # initializing
        output = {
            "ones" : 0,
            "twos" : 0,
            "threes" : 0,
            "fours" : 0,
            "fives" : 0,
            "sixes" : 0,
        }
        # mode: max <------------------------------------------------------------------- continue here
        if mode == "max":
            print(f"mode: {mode}")
            for key, val in self.current_rolls.items():
                if lut_dict[key][str(val)][0] != 0:
                    output[key] = lut_dict[key][str(val)][1]
                    points_increase += lut_dict[key][str(val)][0]
        # mode: daniel
        elif mode == "daniel":
            print(f"mode: {mode}")
        # mode: fail save
        else:
            print("The evaluation mode you set was not valid.")
            return
        # increasing points
        self.points += points_increase
        self.dice_available -= dice_lost
        return





if __name__ == '__main__':
    r = turn()
    r.roll_dice()
    r.show_roll()
    r.eval()

