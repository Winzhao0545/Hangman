class Hangman:
    #Attributes of the class
     #Words to be selected
    def __init__(self) -> None:
        self.possible_words=['becode','learning','mathematics','sessions']
        self.word_to_find=list(random.choice(self.possible_words))
     #players'lives in the game
        self.lives=5
     #letters that are correctly guessed 
        self.correctly_guessed_letters=[]
     #letters that are wrongly guessed
        self.wrongly_guessed_letters=[]
     #numbers played by players
        self.turn_count=0  
     #errors played by players.           
        self.error_count =0           
    #create a method to play the game.
    def play(self):
    
