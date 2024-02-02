#rock_paper_scisors
import random

print('===============================')

print('Rock, Paper, Scissors!')

print('===============================')

print('1.) ✊ Rock')

print('2.) ✋ Paper')

print('3.) ✌️ Scissor')

player = int(input('Pick a number, Rock! Paper! Scissors! SHOOT! '))

computer = random.randint(1,3)

if player == 1 and computer == 3:

  print(f"Player:✊" , player

  , "Computer:✌️" , computer

  ,"Player Wins!"

  )

elif player == 3 and computer == 2:

  print(f"Player:✌️" , player

  , "Computer:✋" , computer

  ,"Player Wins!"

  )

elif player == 2 and computer == 1:

  print(f"Player:✋" , player

  , "Computer:✊" , computer

  ,"Player Wins!"

  )

elif computer == 1 and player == 3:

  print(f"Player:✊" , player

  , "Computer:✌️" , computer

  , "Computer Wins!"

  )

elif computer == 3 and player == 2:

  print(f"Player:✌️" , player

  , "Computer:✋" , computer

  , "Computer Wins!")

elif computer == 2 and player == 1:

  print(f"Player:✋" , player

  , "Computer:✊" , computer

  , "Computer Wins!"

  )

elif computer == 1 and player == 1:

  print(f"Player:✊" , player

  , "Computer:✊" , computer

  ,"Tie!"

  )

elif computer == 2 and player == 2:

  print(f"Player:✋" , player

  , "Computer:✋", computer

  ,"Tie!")

elif computer == 3 and player == 3:

  print(f"Player:✌️" , player

  , "Computer:✌️" , computer

  , "Tie!")

else:

  print("Invalid Input!")
