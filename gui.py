#SUDOKU GAME : GUI  (Graphic User Interface)

# This project is done by Shreyas Ujagar.
# It is a graphic user interface for a sudoku game with assisting features
#  that I thought would be of most help to the user, especially a solver and a checker that provides clear feedback.
#  Pygame is the python library that helped me build this GUI (Graphic User Interface)
# The solver implements a backtrackiing algorithm that recursively fills in the boxes and checks the attempt immediately and
# backtracks when none of the attempts lead to a correct solution.  
# I have only used the following youtube videos that have helped me understand this algorithm and pygame which are cited below.
# This code may not be used without the consent of Shreyas Ujagar.

# I hope you enjoy this project as much as I enjoyed making it :)



# Sources that helped me make this project are below. 

# https://www.youtube.com/watch?v=eqUwSA0xI-s&t=5s

# https://www.youtube.com/watch?v=lK4N8E6uNr4&t=37s
# https://www.youtube.com/watch?v=_Z9Mz2V-Mig
# https://www.youtube.com/watch?v=I2lOwRiGNy4              (I have implemented my sudoku grid and formatted it based on this tutorial)
# https://www.youtube.com/watch?v=IyHb_g2kHDQ




import pygame
import time

 
width = 1000
bgc = (251, 247, 245)
buff = 5
yellow_bg=  (255, 240, 220)
clock = pygame.time.Clock()



# difficulty: EASY
#board1 = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]   
#board2 = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

# difficulty: MEDIUM
#board1 = [[".",".","1","8","4",".",".",".","."],["2",".","4",".","3",".",".",".","1"],[".","7",".","2",".",".",".",".","."],["7","9",".",".",".",".","6",".","."],[".","5",".",".",".",".",".","2","."],[".",".","6",".",".",".",".","9","3"],[".",".",".",".",".","9",".","7","."],["1",".",".",".","8",".","3",".","5"],[".",".",".",".","2","3","4",".","."]]
#board2 = [[".",".","1","8","4",".",".",".","."],["2",".","4",".","3",".",".",".","1"],[".","7",".","2",".",".",".",".","."],["7","9",".",".",".",".","6",".","."],[".","5",".",".",".",".",".","2","."],[".",".","6",".",".",".",".","9","3"],[".",".",".",".",".","9",".","7","."],["1",".",".",".","8",".","3",".","5"],[".",".",".",".","2","3","4",".","."]]

# difficulty: HARD
board1 = [["5",".",".",".",".",".","8",".","."],[".",".",".",".",".","3",".",".","9"],[".",".","1","8",".",".","3",".","."],[".","5",".","3",".",".",".",".","."],[".",".","3",".","9","6",".","8","."],[".","4","7",".","8",".",".","6","."],["3",".",".","9","2",".","5",".","."],[".","1",".",".",".",".",".","7","."],[".",".",".","5","7",".","6",".","4"]]
board2 = [["5",".",".",".",".",".","8",".","."],[".",".",".",".",".","3",".",".","9"],[".",".","1","8",".",".","3",".","."],[".","5",".","3",".",".",".",".","."],[".",".","3",".","9","6",".","8","."],[".","4","7",".","8",".",".","6","."],["3",".",".","9","2",".","5",".","."],[".","1",".",".",".",".",".","7","."],[".",".",".","5","7",".","6",".","4"]]





col_q = (0,153,0) # color of our question numbers


def user(w, position):

    i, j = position[1], position[0]  # get position of left click
    myfont = pygame.font.SysFont('Comic Sans MS', 35)

     # draw a rectangle in yellow to highlight wherever the user has clicked

    pygame.draw.rect(w,(255,255,0) , (position[0]*50+ buff, position[1]*50 + buff, 50- 2*buff, 50-2*buff ))
    pygame.display.update()
   

    if( board1[i-1][j-1]!= "." ): # if user has clicked on a original number
        time.sleep(0.20) 
        pygame.draw.rect(w,bgc , (position[0]*50+ buff, position[1]*50 + buff, 50- 2*buff, 50-2*buff )) # redraw the square
        value = myfont.render(str(board1[i-1][j-1]), True, col_q ) # put that number back in the box
        w.blit(value, (position[0]*50 +15, position[1]*50))
        pygame.display.update()
        return # works perfectly 
        

    while True:
        
        
        clock.tick(60)
        for event in pygame.event.get(): # event after a click could be a key pressed or a quit.
            
             if event.type == pygame.QUIT:
                 pygame.quit()
                 return

             elif event.type ==  pygame.KEYDOWN: ## dont want the skeleton to change from user
                
                if( board1[i-1][j-1]!= "." ): # if user hits skeleton
                    return

                elif(event.key == 115 or event.key == 83): # if user hits solve
                    solveSudoku(board1, w)
                    text = myfont.render("Hope you enjoyed playing!! Have a lovely day :)", False, (0,191,255))
                    pygame.draw.rect(w, bgc, (25, 840, 1000, 500 ))
                    w.blit(text, (25, 840))
                    pygame.display.update() # display the board


                    while True:
                        clock.tick(60)

                        for event in pygame.event.get():
                              if event.type == pygame.QUIT:
                                  pygame.quit()
                                  return


                elif(event.key == 67 or event.key == 99):
                    #print("C is entered. or c after click!")
                    pygame.draw.rect(w,bgc , (position[0]*50+ buff, position[1]*50 + buff, 50- 2*buff, 50-2*buff )) # redraw the square
                    if(board2[i-1][j-1] != "."):
                        value = myfont.render(str(board2[i-1][j-1]), True, (0,0,0) ) # put that user inputted number back in the box
                        w.blit(value, (position[0]*50 +15, position[1]*50))
                        
                    pygame.display.update()
                    check_board(board2, w)

                elif(event.key == 48) : # if user wants to delete an entry and hits 0 
                    board2[i-1][j-1] = "." 
                    pygame.draw.rect(w, bgc, (position[0]*50+ buff, position[1]*50 + buff, 50- 2*buff, 50-2*buff ))
                    pygame.display.update()


                elif(0< event.key-48 <10): # valid input  
                    
                    
                    pygame.draw.rect(w, bgc, (position[0]*50+ buff, position[1]*50 + buff, 50- 2*buff, 50-2*buff )) # makes us edit a square directly
                    value = myfont.render(str(event.key -48 ), True, (0,0,0))
                    w.blit(value, (position[0]*50 +15, position[1]*50))
                    board2[i-1][j-1] = event.key -48
                    pygame.display.update()
                    return
                    


               # simply invalid input by user (eg. user pressed on a letter or any non numerical input )
        
                else:
                    pygame.draw.rect(w,bgc , (position[0]*50+ buff, position[1]*50 + buff, 50- 2*buff, 50-2*buff )) # redraw the square regardless if blank or filled
                    
                    if( board1[i-1][j-1]== "." ): # if user has clicked on an editable square

                        if(board2[i-1][j-1] != "."): # if the user had inputted a number on that square
                            value = myfont.render(str(board2[i-1][j-1]), True, (0,0,0) ) # put that user inputted number back in the box
                            w.blit(value, (position[0]*50 +15, position[1]*50))
                        
                    pygame.display.update()

                return

            
    


def solveSudoku( board, w): # back track
    
        myfont = pygame.font.SysFont('Comic Sans MS', 35)

        def find_empty(board):

            for a in range(9):
                for b in range(9):

                    if(board[a][b] == "."):
                        return a,b

            return None



        def solver(board): ## is board and board2 gonna be the same
           
            
            if(find_empty(board) is None):
                return True

            else:
                i, j = find_empty(board)

                for k in range(1,10):
                    if is_valid(board, i , j , k):
                        board[i][j] = str(k)
                        pygame.draw.rect(w, bgc, ((j+1)*50+ buff, (i+1)*50 + buff, 50- 2*buff, 50-2*buff )) # makes us edit a square directly
                        value = myfont.render(str(k), True, (0,0,0) )
                        w.blit(value, ((j+1)*50 +15, (i+1)*50))## check
                        
                        if(i%8==0 and j % 8 == 0):
                            pygame.display.update()
                        
                        
                        if(solver(board)): # backtrack
                            pygame.display.update()
                            return True

                        else:
                            board[i][j]= "."

                            pygame.draw.rect(w, bgc, ((j+1)*50 + buff, (i+1)*50 + buff, 50- 2*buff, 50-2*buff ))

                return False

        solver(board)

def is_valid_d( w, board, i , j, num, mytruth): # returns true if the number is valid for box at position (i,j)

    # num is an int here!!!!!!

    myfont = pygame.font.SysFont('Comic Sans MS', 35)
    myfont2 = pygame.font.SysFont('Comic Sans MS', 25)

    if(mytruth == False): # just for safety 
    
            for k in range(9): # check all column entries in the same row
                
                if(board[i][k] == "."):
                    continue
                
                if (int(board[i][k]) == num) and (j != k ):

                    # we must make sure that we retain the colors of the question and the user input number  
                    
                    pygame.draw.rect(w, (220,20,60), ((j+1)*50+ buff, (i+1)*50 + buff, 50- 1.5*buff, 50-1.5*buff )) # draw a red square at (i, j)

                    
                    value1 = myfont.render(str(num), True, (0,0,0)) # black again because (i,j) is a user entry 
                        
                    w.blit(value1, ((j+1)*50 +15, (i+1)*50))
                    

                    pygame.draw.rect(w, (220,20,60), ((k+1)*50+ buff, (i+1)*50 + buff, 50- 1.5*buff, 50-1.5*buff )) # draw a red square at i, k


                    if(board1[i][k] == "."): # I know that at [i][k] is not an original position that has a number
                        value2 = myfont.render(str(num), True, (0,0,0))

                    else: # there is a number on original board
                        if(int(board1[i][k]) == num ): 
                            value2 = myfont.render(str(num), True, col_q)
                        
                    w.blit(value2, ((k+1)*50 +15, (i+1)*50))## check

                    pygame.display.update()

                    time.sleep(2)

                    # we must redraw the normal squares back

                    pygame.draw.rect(w, bgc, ((j+1)*50+ buff, (i+1)*50 + buff, 50- 1.5*buff, 50-1.5*buff )) # draw the normal square again at i, j
                    w.blit(value1, ((j+1)*50 +15, (i+1)*50))
                    pygame.draw.rect(w, bgc, ((k+1)*50+ buff, (i+1)*50 + buff, 50- 1.5*buff, 50-1.5*buff )) # draw a normal square again at i, k
                    w.blit(value2, ((k+1)*50 +15, (i+1)*50))

                    pygame.display.update()

                    return False

            for k in range(9): # check column

                if(board[k][j] == ".") : # if empty slot we continue because it does not contradict with anything
                    continue
                
                if (int(board[k][j]) == num) and (i != k ):

                    pygame.draw.rect(w, (220,20,60), ((j+1)*50+ buff, (i+1)*50 + buff, 50- 1.5*buff, 50-1.5*buff )) # draw a red square at i, j
                    value1 = myfont.render(str(num), True, (0,0,0)) # val1 is always black          
                    w.blit(value1, ((j+1)*50 +15, (i+1)*50))

                    pygame.draw.rect(w, (220,20,60), ((j+1)*50+ buff, (k+1)*50 + buff, 50- 1.5*buff, 50-1.5*buff )) # draw a red square at k, j

                    if(board1[k][j] == "."): #  know that at [k][j] is not an original position that has a number
                        value2 = myfont.render(str(num), True, (0,0,0))

                    else: # there is a number on original board
                        if(int(board1[k][j]) == num ): # can delete 
                            value2 = myfont.render(str(num), True, col_q)
                        
                    w.blit(value2, ((j+1)*50 +15, (k+1)*50))

                    pygame.display.update()

                    time.sleep(2)
                    
                     # we must redraw the normal squares back

                    pygame.draw.rect(w, bgc, ((j+1)*50+ buff, (i+1)*50 + buff, 50- 1.5*buff, 50-1.5*buff )) # draw the normal square again at i, j
                    w.blit(value1, ((j+1)*50 +15, (i+1)*50))
                    
                    pygame.draw.rect(w, bgc, ((j+1)*50+ buff, (k+1)*50 + buff, 50- 1.5*buff, 50-1.5*buff )) # draw a normal square again at k, j
                    w.blit(value2, ((j+1)*50 +15, (k+1)*50))

                    pygame.display.update()
                    return False

            
             # now we check the 3x3 square validity
            index_x  = i//3
            index_y = j//3

            for m in range(index_x *3 , (index_x *3) + 3):
                for n in range(index_y *3 , (index_y *3) + 3):

                    if(board[m][n] == "."):
                        continue

                    if(int(board[m][n]) == num) and (m != i or n !=j):
                         

                         pygame.draw.rect(w, (220,20,60), ((j+1)*50+ buff, (i+1)*50 + buff, 50- 1.5*buff, 50-1.5*buff )) # draw a red square at i, j

                         value1 = myfont.render(str(num), True, (0,0,0))
                         w.blit(value1, ((j+1)*50 +15, (i+1)*50))

                         pygame.draw.rect(w, (220,20,60), ((n+1)*50+ buff, (m+1)*50 + buff, 50- 1.5*buff, 50-1.5*buff )) # draw a red square at m, n

                         if(board1[m][n] == "."): #  know that at [m][n] is not an original position that has a number
                             value2 = myfont.render(str(num), True, (0,0,0))

                         else: # there is a number on original board

                             if(int(board1[m][n]) == num ): # can delete

                                 value2 = myfont.render(str(num), True, col_q)
                        

                         w.blit(value2, ((n+1)*50 +15, (m+1)*50))

                         pygame.display.update()

                         time.sleep(2)
                    
                     # we must redraw the normal squares back

                         pygame.draw.rect(w, bgc, ((j+1)*50+ buff, (i+1)*50 + buff, 50- 1.5*buff, 50-1.5*buff )) # draw the normal square again at i, j
                         w.blit(value1, ((j+1)*50 +15, (i+1)*50))## check
                        
                         pygame.draw.rect(w, bgc, ((n+1)*50+ buff, (m+1)*50 + buff, 50- 1.5*buff, 50-1.5*buff )) # draw a normal square again at m, n
                         w.blit(value2, ((n+1)*50 +15, (m+1)*50))## check

                         pygame.display.update()
                         return False

            return True



def is_valid( board, i , j, num): # returns true if the number is valid for box at position (i,j)

    
            for k in range(9): # check all column entries in the same row
                if (board[i][k] == str(num)) and (j != k ):
                    return False

            for k in range(9): # check column
                if (board[k][j] == str(num)) and (i != k ):
                    return False

            index_x  = i//3
            index_y = j//3

            for m in range(index_x *3 , (index_x *3) + 3):
                for n in range(index_y *3 , (index_y *3) + 3):

                    if((board[m][n] == str(num)) and (m != i or n !=j)):
                        return False

            return True


def check_board(board, w): ## tells you if your board is in a solved state // called in board 2

    myfont = pygame.font.SysFont('Comic Sans MS', 35)
    myfont2 = pygame.font.SysFont('Comic Sans MS', 25)
    
    for i in range(9):
        for j in range(9):

            if(board1[i][j] != "."): # if the initial board has a number on [i][j]
                continue # we dont need to check if our original number is valid
                
            
# i, j has to be a user entry at this point
# dealing with blank squares or user inputs

            if(board[i][j] != "."): # if user has inputted a number here, we want to check is that is valid.
                if not is_valid_d(w, board, i, j, int(board[i][j]), False): ## if there is a position that is not valid in user's attempt. We have sent in board2

                    text = myfont.render("Feedback: Your attempt is incorrect. Look at the box", False, (255,0,0))
                    pygame.draw.rect(w, bgc, (25, 840, 1000, 500 ))
                    w.blit(text, (25, 840))

                    text = myfont.render("at row " + str(i+1) + " and column " + str(j+1), False, (255,0,0) )
                    w.blit(text, (25, 880))
                    pygame.display.update() # display the board
                    
                    return

# out of the for loops
    
    for i in range(9):
        for j in range(9):
            if(board[i][j] == "."): # if we have found an empty cell but nothing the user did was incorrect so far
                

                text = myfont.render("Feedback: So far so good! ", False, (0,0,237))
                pygame.draw.rect(w, bgc, (25, 840, 1000, 500 ))
                w.blit(text, (25, 840)) 

                pygame.draw.rect(w, (220,20,60), ((j+1)*50+ buff, (i+1)*50 + buff, 50- 1.5*buff, 50-1.5*buff )) # draw a red square at the first empty cell
                pygame.display.update() # display the board
                time.sleep(1.5)
                pygame.draw.rect(w, bgc, ((j+1)*50+ buff, (i+1)*50 + buff, 50- 1.5*buff, 50-1.5*buff )) # draw back a white square
                pygame.display.update() # display the board    
                return


 # we have validated each non empty cell already. We also know there is no empty cell left. Thus the user has solved the board. 
        
    text = myfont.render("Feedback: YOU WIN!! Go treat yourself!! You earned it!", False, (0,255,0))
    pygame.draw.rect(w, bgc, (25, 840, 1000, 500 ))
    w.blit(text, (25, 840))

    pygame.display.update() # display the board
                            
    return



   

    

                                
def main():
    pygame.init()
    w = pygame.display.set_mode((width,width)) # window 
    pygame.display.set_caption("Shreyas's Sudoku Challenge")
    w.fill(bgc)
    w.fill(yellow_bg, (500, 0, 500, 507))
    w.fill(yellow_bg, (0, 0, 500, 50))
    w.fill(yellow_bg, (0, 0, 50, 510))
    
    
    myfont = pygame.font.SysFont('Comic Sans MS', 35)
    myfont2 = pygame.font.SysFont('Comic Sans MS', 25)
    
    
    
    for i in range(0,10): # draw lines of our board

        if(i%3 == 0 ): # make every third line extra wide so we can split up our board into 9 sub boxes
             pygame.draw.line(w, (0,0,0), (50 +50*i, 50),(50 +50*i, 500),6)
             pygame.draw.line(w, (0,0,0), (50, 50+50*i ),(500, 50 + 50*i),6)

        else:
            pygame.draw.line(w, (0,0,0), (50 +50*i, 50),(50 +50*i, 500),2)
            pygame.draw.line(w, (0,0,0), (50, 50+50*i ),(500, 50 + 50*i),2)

 


  

    
    for i in range(9):
        for j in range(9): ## put in values to our board 
            if(board1[i][j]!= "."):
                val = myfont.render(board1[i][j], True, col_q) # val is a surface that we will blit onto window w  
                w.blit(val, ((j+1)*50 +15, (i+1)*50  )) 

    pygame.display.update()


    text = myfont.render("Shreyas's Sudoku Challenge", False, (0,0,0) )
    w.blit(text, (150, 550))
    

    text = myfont2.render("The goal of Sudoku is to fill the 9x9 grid with digits so that every row, column, ", False, (0,0,0))
    w.blit(text, (25, 625))
    

    text = myfont2.render("and 3x3 square have the numbers 1-9 each, exactly once and no number should", False, (0,0,0) )
    w.blit(text, (25, 670))
    

    text = myfont2.render("repeat. Use logic, the process of elimination and the already placed numbers as", False, (0,0,0) )
    w.blit(text, (25, 715))
    

    text = myfont2.render("clues to fill the empty spaces! Can you solve Shreyas's challenge?", False, (0,0,0) )
    w.blit(text, (25, 760))

    text = myfont.render("How to play", False, (0,0,0) )
    w.blit(text, (620, 20))
    
    text = myfont2.render("Click on an empty box. Type a digit.", False, (0,0,0) )
    
    w.blit(text, (560, 100))

    text = myfont2.render("To remove an entered digit, click", False, (0,0,0) )
    w.blit(text, (560, 160))
    text = myfont2.render("on the appropriate box and type '0'. ", False, (0,0,0) )
    w.blit(text, (565, 190))
    text = myfont2.render("To (c)heck your progress, ", False, (0,0,0) )
    w.blit(text, (560, 250))
    text = myfont2.render("press the 'c' key. (feedback is ", False, (0,0,0) )
    w.blit(text, (560, 280))
    text = myfont2.render("below)", False, (0,0,0))
    w.blit(text, (560, 310))
    
    text = myfont2.render("Psssst!!!    If you are a tad bit lazy, ", False, (0,0,0) )
    w.blit(text, (560, 390)) 

    text = myfont2.render("just hit 's' and I will (s)olve it", False, (0,0,0) )
    w.blit(text, (560, 420 )) 

    text = myfont2.render("for you :)", False, (0,0,0) )
    w.blit(text, (560, 450))


    text = myfont.render("Feedback: (you have not begun yet)", False, (0,191,255))
    w.blit(text, (25, 840))

    # draw umbrella and rain drops
    pygame.draw.circle(w, (120,81,21), (800,570), 40, 3, True, True, False, False)
    pygame.draw.line(w, (120,81,21), (760, 570), (840, 570), 3)
    pygame.draw.line(w, (120,81,21), (800, 570), (800, 620), 3)
    pygame.draw.circle(w, (120,81,21), (800,608), 15, 3, False, False, False, True)
    pygame.draw.line(w, (65,105,225), (760, 540), (760, 550), 3)
    pygame.draw.line(w, (65,105,225), (780, 530), (780, 520), 3)
    pygame.draw.line(w, (65,105,225), (770, 525), (770, 535), 3)
    pygame.draw.line(w, (65,105,225), (800, 510), (800,520), 3)
    pygame.draw.line(w, (65,105,225), (815, 510), (815, 520), 3)
    pygame.draw.line(w, (65,105,225), (830, 530), (830, 520), 3)
    pygame.draw.line(w, (65,105,225), (750, 600), (750,610), 3)
    pygame.draw.line(w, (65,105,225), (740, 600), (740, 610), 3)
    pygame.draw.line(w, (65,105,225), (730, 590), (730, 600), 3)
    pygame.draw.line(w, (65,105,225), (750, 500), (750,510), 3)
    pygame.draw.line(w, (65,105,225), (740, 510), (740, 520), 3)
    pygame.draw.line(w, (65,105,225), (730, 520), (730, 530), 3)
    pygame.draw.line(w, (65,105,225), (750, 530), (750,540), 3)
    pygame.draw.line(w, (65,105,225), (740, 540), (740, 550), 3)
    pygame.draw.line(w, (65,105,225), (730, 550), (730, 560), 3)
    pygame.draw.line(w, (65,105,225), (750, 560), (750,570), 3)
    pygame.draw.line(w, (65,105,225), (740, 570), (740, 580), 3)
    pygame.draw.line(w, (65,105,225), (730, 580), (730, 590), 3)
    pygame.draw.line(w, (65,105,225), (850, 530), (850,540), 3)
    pygame.draw.line(w, (65,105,225), (860, 540), (860, 550), 3)
    pygame.draw.line(w, (65,105,225), (870, 550), (870, 560), 3)
    pygame.draw.line(w, (65,105,225), (895, 560), (895,570), 3)
    pygame.draw.line(w, (65,105,225), (900, 572), (900, 580), 3)
    pygame.draw.line(w, (65,105,225), (920, 580), (920, 590), 3)
    pygame.draw.line(w, (65,105,225), (850, 550), (850,560), 3)
    pygame.draw.line(w, (65,105,225), (860, 560), (860, 570), 3)
    pygame.draw.line(w, (65,105,225), (870, 570), (870, 580), 3)
    pygame.draw.line(w, (65,105,225), (895, 580), (895,590), 3)
    pygame.draw.line(w, (65,105,225), (895, 580), (895,590), 3)
    pygame.draw.line(w, (65,105,225), (900, 582), (900, 590), 3)
    pygame.draw.line(w, (65,105,225), (920, 590), (920, 600), 3)
    pygame.draw.line(w, (65,105,225), (850, 600), (850,610), 3)
    pygame.draw.line(w, (65,105,225), (855, 603), (855,613), 3)
    pygame.draw.line(w, (65,105,225), (868, 600), (868,610), 3)
    pygame.draw.line(w, (65,105,225), (870, 520), (870,530), 3)
    pygame.draw.line(w, (65,105,225), (880, 520), (880,530), 3)
    pygame.draw.line(w, (65,105,225), (890, 520), (890,530), 3)
    pygame.draw.line(w, (65,105,225), (920, 520), (920,530), 3)
    pygame.draw.line(w, (65,105,225), (920, 520), (920,530), 3)
    pygame.draw.line(w, (65,105,225), (910, 520), (910,530), 3)
    pygame.draw.line(w, (65,105,225), (920, 530), (920,540), 3)
    pygame.draw.line(w, (65,105,225), (920, 535), (920,545), 3)
    pygame.draw.line(w, (65,105,225), (910, 555), (910,565), 3)
    pygame.draw.line(w, (65,105,225), (895, 535), (895,545), 3)
    pygame.draw.line(w, (65,105,225), (885, 535), (885,545), 3)
    pygame.draw.line(w, (65,105,225), (895, 595), (895,605), 3)
    pygame.draw.line(w, (65,105,225), (885, 597), (885,607), 3)
    pygame.draw.line(w, (65,105,225), (848, 570), (848,580), 3)

    pygame.display.update() # display the board

   
 
    while True:
        clock.tick(60)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1: #if there is left click
                pos = pygame.mouse.get_pos() # get coordinates of that click

                if(pos[0]<50 or pos[0]>500 or pos[1]<50 or pos[1]>500 ): # if user clicks outside the grid we do not do anything
                    continue

                user(w, (pos[0]//50, pos[1]//50))# call to user function when there is a click on the board


            
            if event.type ==  pygame.KEYDOWN: ## if there was a direct key pressed w/o a click

                if(event.key == 115 or event.key == 83): # if that key was for solve
                    solveSudoku(board1, w)
                    text = myfont.render("Hope you enjoyed playing!! Have a lovely day :)", False, (0,191,255))
                    pygame.draw.rect(w, bgc, (25, 840, 1000, 500 ))
                    w.blit(text, (25, 840))
                    pygame.display.update() # display the board


                    while True:
                        clock.tick(60)

                        for event in pygame.event.get():
                              if event.type == pygame.QUIT:
                                  pygame.quit()
                                  return

                    

                  
                    

                if(event.key == 67 or event.key == 99): # if that key is for check
                    check_board(board2, w) # want to check the user's board

                
                


main()



