#import string, random
PICS = ['''


    +---+

    |   |

        |

       |

        |

        |

 =========''', '''



   +---+

   |   |

   O   |

       |

       |

       |

 =========''', '''



   +---+

   |   |

   O   |

   |   |

       |

       |

 =========''', '''



   +---+

   |   |

   O   |

  /|   |

       |

       |

 =========''', '''



   +---+

   |   |

   O   |

  /|\  |

      |

      |

 =========''', '''



   +---+

   |   |

   O   |

  /|\  |

  /    |

       |

 =========''', '''



   +---+

   |   |

   O   |

  /|\  |

  / \  |

       |

 =========''']
secret_word='apple'

#helper functipons
def is_word_guessed(secret_word, letters_guessed):
  correct_letter = 0
  for char in secret_word:
     if char == letters_guessed:
        correct_letter +=1
        if correct_letter == len(secret_word):
          return True
        else:
          return False

def get_guessed_word(secret_word, letters_guessed):
  correct_letters=[]
  guessed_str=''
  for char in letters_guessed:
    if char in secret_word:
      correct_letters.append(char)

  for char in secret_word:
    if char in correct_letters:
      guessed_str+=char
    else:
      guessed_str+="_ "
  return guessed_str


def get_available_letters(letters_guessed):

    #first get all available letters in lowercase
    letters = string.ascii_lowercase
    unguessed = ""
    #for each item in letters, check if it's been guessed; if not, added to unguessed variable
    for char in letters:
      if char not in letters_guessed:
        unguessed += char
    return unguessed

def warnings_check(warnings_left,guess,dublicate,show_word,):
  warnings_left-=1
  if not guess.isalpha():
    print('oh no, this is not a letter, you have '+str(warnings_left)+'  warnings'+show_word)
  elif guess in dublicate:
    print('oh no, you tried this alredy, you have' +str(warnings_left)+'  warnings left'+show_word)
    print("_"*22)
  return warnings_left

# checking how many guesses we have left/avoiding repetition
def guesses_check(guesses_left,guess,dublicate,show_word):
  guesses_left-=1
  if not guess.isalpha():
    print('oh no, this is not a letter, you have  '+str(guesses_left)+'  guesses '+show_word)
  elif guess in dublicate:
    print('you have tried this alredy now you have '+str(guesses_left)+'  guesses '+show_word)
    print("_"*22)
  return guesses_left

def hangman(seret_word):
  #unique_letters=''
  letters_guessed=[]
  dublicate=[] #for letters and etc
  guesses_left=7
  warnings_left=3
  show_word="_"*len(secret_word)
  answer = get_guessed_word(secret_word, letters_guessed)
  i=0

  print('welcome to the game HANGMAN')
  print('i\'m thinking of the word that is '+str(len(secret_word))+' long')
  print(12*"_")

  while warnings_check(warnings_left,guess,dublicate,show_word)>0:
    print(PICS[i])
    print('You have ',warnings_check(warnings_left,guess,dublicate,show_word),'warnings left.'  )
    print('You have ',guesses_check(guesses_left,guess,dublicate,show_word),'warnings left.'  )
    print('your  clues are: ',get_available_letters(letters_guessed))
    guess = str.lower(input("Please enter a letter. ")

    if guess.isalpha() == False :
      warnings_check(warnings_left,guess,dublicate,show_word)
    elif guess in letters_guessed:
      guesses_check(guesses_left,guess,dublicate,show_word)
    else:
      letters_guessed.append(guess)
      new_answer = get_guessed_word(secret_word, letters_guessed)
       if answer != new_answer:
        print(f"Good guess. {new_answer}")
        if is_word_guessed(secret_word, letters_guessed)== True:
          print('winner')
          break
   dublicate.append(guess)
