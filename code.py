from turtle import *
import math
import random
import time

win = Screen()
def game(speedOfgoals , speedLevel , numOfObstacle , level , name , player_score , size):
   
    win.bgcolor("black")
    win.title("Turtle Game!")
    win.setup(width=700, height=700)
    
    if(level == 1):
        name = win.textinput("Player Name", "Move with Left and Right\n Esc for end game \n\nEnter your name: ")
    win.tracer(3)


    # Draw a border tion
    border = Turtle()
    border.penup()
    border.color("white" , "#55aaaa")
    border.begin_fill()
    border.setposition(-300 , -300)
    border.pendown()
    border.pensize(3)
    for side in range(4):
        border.forward(600)
        border.left(90)
    
    border.end_fill()
    border.hideturtle()


    # Create player 
    player = Turtle()
    player.color("#226666");
    player.shape("turtle")
    player.penup()
    player.speed(0) # animation speed



    # create goals
    maxGoals = 5
    goals = []
    colors = ["#b49fd8" , "#f94f8a" , "#45954c" , "#baffef"  , "#ffbdbd" , "#77dd77" , "#faa9a9" , "#bfe7ff"]
    for i in range(maxGoals):
        goals.append(Turtle())
        goals[i].shape("circle")  
        goals[i].color(colors[random.randint(0 , 7)])
        goals[i].penup()
        goals[i].speed(0)
        goals[i].setposition(random.randint(-300, 300) , random.randint(-300 , 300))
        goals[i].color()

    # Set speed  (movement speed)
    speed = speedLevel

    # create the score variable 
    score = player_score    



    # Define functions

    def TurnLeft():
        player.left(30)
    
    def TurnRight():
        player.right(30)
    
 


    def IsCollision(t1 , t2):
        d = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2) )
        if d <= 20:
            return True
        else:
            return False
    
    def gameover():
        over = Turtle()
        win.clear()
        win.bgcolor("#00b8ff")
        over.color("#001f2b")
        over.pensize(10)
        over.hideturtle()
        over.goto(30, -100)
        over.write(f"Game Over\n{name}\nYour score: {score } ", align="center", font=("Courier", 35, "normal"))
        time.sleep(3)
        over.clear()
        
    def closeGame():
        gameover()  
        win.bye()
        exit()
    


    def play_again():
        gameover()
        answer = win.textinput("Play Again ?" , "enter \"yes\" if you want to play again")
        if answer == "yes":
             game( 1.5 , 2.5  ,  0 , 1  , "unknown" , 0 , 0)
        
        else:
            closeGame()
    

    def levelUp():
        win.clear()
        game(speedOfgoals + 0.5 , speedLevel + 0.5 , numOfObstacle + 2 , level + 1 , name , score , 0)
        
    def escape():
        win.bye()
        exit()
    
    #Set Keyboard bindings
    listen()
    onkey(TurnLeft , "Left")
    onkey(TurnRight , "Right")
    onkeypress(escape, "Escape")

    # set a timer 
    timer_turtle = Turtle()
    timer_turtle.hideturtle()
    timer_turtle.penup()
    timer_turtle.goto(100 , 310)
    timer_turtle.color("white")

    def update_timer(seconds):
        timer_turtle.clear()
        timer_turtle.write(f"Time: {seconds} seconds", align="center", font=("Arial", 16, "normal"))


    start_time = time.time()
    game_duration = 30  # Set the duration of the game in seconds



    # Create obstacle   
    obstacles = []
    numOfObstacle
    for i in range(numOfObstacle):
        obstacles.append( Turtle())
        obstacles[i].speed(0)
        obstacles[i].shape("triangle")
        obstacles[i].color("black")
        obstacles[i].penup()
        obstacles[i].setposition(random.randint(-280, 280) , random.randint(-280 , 280)) 
        obstacles[i].shapesize(stretch_wid= 1.2 , stretch_len = 1.2)


    
    while True:
   
        elapsed_time = time.time() - start_time
        # Check if time is up
        if elapsed_time >= game_duration:
           levelUp()

        # Update and display the timer
        update_timer(int(game_duration - elapsed_time))
        

        player.forward(speed)
   

    
        # Boundary Checking 
        if player.xcor() > 300 or player.xcor() < -300:
            player.right(180) # turn around
        
        if player.ycor() > 300 or player.ycor() < -300:
            player.right(180) # turn around
    
        #Draw the score on the screen
        border.undo()
        border.penup()
        border.hideturtle()
        border.setposition(-200 , 310)
        scorestring = "Score: %s "%(score)
        scorestring += "   Level: %s "%(level)
        border.write(scorestring , False , align = "left" , font = ("Arial" , 14 , "normal"))
        


        # move the goal
        for i in range(maxGoals):
            goals[i].forward(speedOfgoals)
        
            # Boundary Checking 
            if goals[i].xcor() > 285 or goals[i].xcor() < -285:
                goals[i].right(180) # turn around
        
            if goals[i].ycor() > 285 or goals[i].ycor() < -285:
                goals[i].right(180) # turn around
            
        
        
        
            # Collision
            if IsCollision(player , goals[i]):
                goals[i].setposition(random.randint(-280, 280) , random.randint(-280 , 280))
                goals[i].right(random.randint(0 , 360)) 
                goals[i].color(colors[random.randint(0 ,7)])
            
                score += 10
                size += 1
                player.shapesize(stretch_wid= 1 + 0.2*size, stretch_len=1 + 0.2*size)

        
               
                
            
                
            for j in range(numOfObstacle):       
                if IsCollision(goals[i] ,obstacles[j]): 
                    goals[i].right(180)
       
        for i in range(numOfObstacle):       
            if IsCollision(player ,obstacles[i]):   
                play_again()
        
            

    
        
def main():

    game( 1.5 , 2.5  ,  0 , 1  , "unknown" , 0 , 0)

            
                 
main()

          
            



