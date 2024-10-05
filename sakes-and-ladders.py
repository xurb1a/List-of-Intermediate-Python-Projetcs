#simple python project that works on Condition spam for ladders and snakes and Turtle module to track the dot behavior, you can find the image I worked with or rather based the program upon with the file, you need to change the path of the picture in the code down below to its path on your system





import turtle
import random

screen = turtle.Screen()

def movePlayer(player, position):
   yPos = (position-1) // 10
   xPos = (position-1) % 10
   y = -170 + yPos * 37
   if yPos%2 == 0:
      x = -170 + xPos * 38
   else:
      x = 170 - xPos * 38
   player.goto(x,y)


screen.setup(400, 400)
screen.bgpic("/home/hp/Images/snakes-and-ladders.png")

player1 = turtle.Turtle()
player1.shape("circle")
player1.speed(5)
player1.color("#810081")
player1.pensize(15)
player1.penup()

player1Position = 1
movePlayer(player1, player1Position)

gameOver=False
while not gameOver:
   print("Player 1:")
   input("Press enter to throw the dice...")
   dice = random.randint(1,6)
   print("You've rolled a " + str(dice))
   player1Position = player1Position + dice
   movePlayer(player1, player1Position)
   if player1Position == 5:
      print("Climbing up the ladder!")
      player1Position = 35
   elif player1Position == 8:
      print("Climbing up the ladder!")
      player1Position = 13
   elif player1Position == 11:
      print("Climbing up the ladder!")
      player1Position = 52
   elif player1Position == 21:
      print("Climbing up the ladder!")
      player1Position = 41
   elif player1Position == 59:
      print("Climbing up the ladder!")
      player1Position = 83
   elif player1Position == 85:
      print("Climbing up the ladder!")
      player1Position = 96
   elif player1Position == 72:
      print("Climbing up the ladder!")
      player1Position = 91
   elif player1Position == 36:
      print("Climbing up the ladder!")
      player1Position = 22
   elif player1Position == 68:
      print("Climbing up the ladder!")
      player1Position = 48
   elif player1Position == 63:
      print("Climbing up the ladder!")
      player1Position = 41
   elif player1Position == 84:
      print("Climbing up the ladder!")
      player1Position = 66
   elif player1Position == 93:
      print("Climbing up the ladder!")
      player1Position = 86
  
   if player1Position>100:
      player1Position = 100 - (player1Position-100)
    
   print("Player 1 position: " + str(player1Position))
   movePlayer(player1, player1Position)
  
   if player1Position == 100:
      print("---- Player 1 wins!!! ----")
      gameOver = True
