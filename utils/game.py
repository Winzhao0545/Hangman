import random

class Hangman:
  """
  Function that initiate the class.
  """
  def __init__(self):
    self.possible_words=['becode','learning','mathematics','sessions']
    self.word_to_find=random.choice(self.possible_words)
    self.lives=5
    self.correctly_guess_letter=["_"]*len(self.word_to_find)
    self.wrongly_guess_letter=[]
    self.turn_count=0
    self.error_count=0
  
    
  def play(self):
    """
    Function that ask people to enter letters:
    -Enter ONE letter
    -If right goes to correctly_guess_letter
    -If wrong, letter goes to wrongly_guessed_letters
    """
    
    Input=''
    ask=True
    while ask:
      Input=input("Enter a single letter:")




      #Enter ONE letter
      print(len(Input))
      
      if len(Input)==1:
        ask=False
        print(Input.lower())
       
      
      
        
      else:
        print('Enter a single letter to continue')
        


    #  correct word goes into    
    for i in self.word_to_find:
    
      if Input==i:
        self.correctly_guess_letter.append(i)
        print(self.correctly_guess_letter)
        self.turn_count +=1
        

      else:
        self.wrongly_guess_letter.append(i)
        print(self.wrongly_guess_letter)
        self.error_count +=1
        self.lives-=1
      if Input==self.word_to_find:
        self.well_play()


  def start_game(self):
    """
    Function that start to play the loop of game.
    """
    print("Welcome to Hangman.")
    self.play()
    
    print(self.correctly_guess_letter) 
    print(self.wrongly_guess_letter)
    print(self.lives)
    print(self.error_count) 
    print(self.turn_count)
    #user guess the word→ input = word_to_find 
   
    print('Congratuations, you win the game!')
    #Game over→livers=0
    
      
  def game_over(self):
      if self.lives==0:   
        print('game over.')
    
  def well_play(self):
    print(f'You find the word: ,{self.word_to_find},in,{self.turn_count},turns with,{self.liveserror_count},errors')

    


  
