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


def draw_board(w):

    for i in range(0,10): # draw lines of our board

        if(i%3 == 0 ): # make every third line extra wide so we can split up our board into 9 sub boxes
             pygame.draw.line(w, (0,0,0), (50 +50*i, 50),(50 +50*i, 500),6)
             pygame.draw.line(w, (0,0,0), (50, 50+50*i ),(500, 50 + 50*i),6)

        else:
            pygame.draw.line(w, (0,0,0), (50 +50*i, 50),(50 +50*i, 500),2)
            pygame.draw.line(w, (0,0,0), (50, 50+50*i ),(500, 50 + 50*i),2)
    

 
    
 
width = 1000
bgc = (251, 247, 245)
buff = 5
break_out = True

yellow_bg=  (255, 240, 220)
clock = pygame.time.Clock()


# difficulty: EASY
myboard7 = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]   
myboard8 = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
myboard9 = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]


myboard10 = [["2",".",".",".",".",".",".",".","9"],[".","8","9","2",".","6","3","7","."],[".",".","3",".","5",".","8",".","."],["9",".","5",".",".",".","4",".","7"],[".",".",".","9",".","7",".",".","."],["7",".","6",".",".",".","1",".","3"],[".",".","8",".","6",".","5",".","."],[".","1","2","3",".","4","7","6","."],["4",".",".",".",".",".",".",".","2"]]
myboard11 = [["2",".",".",".",".",".",".",".","9"],[".","8","9","2",".","6","3","7","."],[".",".","3",".","5",".","8",".","."],["9",".","5",".",".",".","4",".","7"],[".",".",".","9",".","7",".",".","."],["7",".","6",".",".",".","1",".","3"],[".",".","8",".","6",".","5",".","."],[".","1","2","3",".","4","7","6","."],["4",".",".",".",".",".",".",".","2"]]
myboard12 = [["2",".",".",".",".",".",".",".","9"],[".","8","9","2",".","6","3","7","."],[".",".","3",".","5",".","8",".","."],["9",".","5",".",".",".","4",".","7"],[".",".",".","9",".","7",".",".","."],["7",".","6",".",".",".","1",".","3"],[".",".","8",".","6",".","5",".","."],[".","1","2","3",".","4","7","6","."],["4",".",".",".",".",".",".",".","2"]]

# difficulty: MEDIUM
myboard4 = [[".",".","1","8","4",".",".",".","."],["2",".","4",".","3",".",".",".","1"],[".","7",".","2",".",".",".",".","."],["7","9",".",".",".",".","6",".","."],[".","5",".",".",".",".",".","2","."],[".",".","6",".",".",".",".","9","3"],[".",".",".",".",".","9",".","7","."],["1",".",".",".","8",".","3",".","5"],[".",".",".",".","2","3","4",".","."]]
myboard5 = [[".",".","1","8","4",".",".",".","."],["2",".","4",".","3",".",".",".","1"],[".","7",".","2",".",".",".",".","."],["7","9",".",".",".",".","6",".","."],[".","5",".",".",".",".",".","2","."],[".",".","6",".",".",".",".","9","3"],[".",".",".",".",".","9",".","7","."],["1",".",".",".","8",".","3",".","5"],[".",".",".",".","2","3","4",".","."]]
myboard6 = [[".",".","1","8","4",".",".",".","."],["2",".","4",".","3",".",".",".","1"],[".","7",".","2",".",".",".",".","."],["7","9",".",".",".",".","6",".","."],[".","5",".",".",".",".",".","2","."],[".",".","6",".",".",".",".","9","3"],[".",".",".",".",".","9",".","7","."],["1",".",".",".","8",".","3",".","5"],[".",".",".",".","2","3","4",".","."]]

# difficulty: HARD
myboard1 = [["5",".",".",".",".",".","8",".","."],[".",".",".",".",".","3",".",".","9"],[".",".","1","8",".",".","3",".","."],[".","5",".","3",".",".",".",".","."],[".",".","3",".","9","6",".","8","."],[".","4","7",".","8",".",".","6","."],["3",".",".","9","2",".","5",".","."],[".","1",".",".",".",".",".","7","."],[".",".",".","5","7",".","6",".","4"]]
myboard2 = [["5",".",".",".",".",".","8",".","."],[".",".",".",".",".","3",".",".","9"],[".",".","1","8",".",".","3",".","."],[".","5",".","3",".",".",".",".","."],[".",".","3",".","9","6",".","8","."],[".","4","7",".","8",".",".","6","."],["3",".",".","9","2",".","5",".","."],[".","1",".",".",".",".",".","7","."],[".",".",".","5","7",".","6",".","4"]]
myboard3 = [["5",".",".",".",".",".","8",".","."],[".",".",".",".",".","3",".",".","9"],[".",".","1","8",".",".","3",".","."],[".","5",".","3",".",".",".",".","."],[".",".","3",".","9","6",".","8","."],[".","4","7",".","8",".",".","6","."],["3",".",".","9","2",".","5",".","."],[".","1",".",".",".",".",".","7","."],[".",".",".","5","7",".","6",".","4"]]





allboards = [myboard1,myboard2,myboard3, myboard4, myboard5,myboard6, myboard7, myboard8,myboard9 ,myboard10,myboard11, myboard12 ]
is_solved = [False, False, False, False] 

board1 = allboards[0]
board2 = allboards[1]
board3 = allboards[2]

board_tracker = 0

pos_x_forthewin = 0
pos_y_forthewin = 0
want_to_quit = False 


col_q = (0,153,0) # color of our original clues on the board is green

pygame.init()
w = pygame.display.set_mode((width,width)) # window for pygame
pygame.display.set_caption("Shreyas's Sudoku Challenge") 
w.fill(bgc)
w.fill(yellow_bg, (500, 0, 500, 507))
w.fill(yellow_bg, (0, 0, 500, 50))
w.fill(yellow_bg, (0, 0, 50, 510))
    
myfont = pygame.font.SysFont('arialunicode', 35) 
myfont2 = pygame.font.SysFont('arialunicode', 25)

draw_board(w)


for i in range(9):
    for j in range(9): ## put values to our board 
        if(board1[i][j]!= "."):
            val = myfont.render(board1[i][j], True, col_q) # val is a surface that we will blit onto window w  
            w.blit(val, ((j+1)*50 +15, (i+1)*50  )) 




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

text = myfont2.render("Psssst!!! If you are a tad bit lazy, ", False, (0,0,0) )
w.blit(text, (560, 390)) 

text = myfont2.render("just hit 's' and I will (s)olve it", False, (0,0,0) )
w.blit(text, (560, 420 )) 

text = myfont2.render("for you :)", False, (0,0,0) )
w.blit(text, (560, 450))


text = myfont.render("Feedback: (you have not begun yet)", False, (0,191,255))
w.blit(text, (25, 840))

# draw_raindrops and umbrella 
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



# Draw 'Try another' button
pygame.draw.rect(w, (122,200,54), (810,760, 156,40))
text = myfont2.render("Try another", False, (0,0,0) )
w.blit(text, (820, 760))


pygame.display.update() # display the board


# This function takes place whenever a user clicks on the board
def user(w, position):

    global board1
    global board2
    global board3
    global break_out
    global board_tracker
    global is_solved
    global want_to_quit 
    
    break_out = True
    i, j = position[1], position[0]  # get position of left click
    global myfont

    
     # drawing a rectangle in yellow to highlight wherever the user has clicked
    pygame.draw.rect(w,(255,255,0) , (position[0]*50 + buff, position[1]*50 + buff, 50 - 2* buff, 50- 2* buff))
    
    pygame.display.update()
    
    if(is_solved[board_tracker//3] == False): 
        if( board1[i-1][j-1]!= "." ): # if user has clicked on a original number we cannot allow them to edit it. 
            time.sleep(0.20)
            pygame.draw.rect(w,bgc , (position[0]*50 + buff, position[1]*50 + buff, 50 - 2* buff, 50 - 2* buff)) # redraw the square
            value = myfont.render(str(board1[i-1][j-1]), True, col_q ) # put that number back in the box
            w.blit(value, (position[0]*50 +15, position[1]*50))
            pygame.display.update()
            return 

    else: # board has been solved so we need to use board3 as our original board so we input numbers in their correct font color.
        
        time.sleep(0.20)
        if(board3[i-1][j-1] != "." ): # if user has clicked on an original number
            
            pygame.draw.rect(w,bgc , (position[0]*50 + buff, position[1]*50 + buff, 50 - 2* buff, 50 - 2* buff)) # redraw the square
            value = myfont.render(str(board3[i-1][j-1]), True, col_q ) # put that number back in the box in the correct font color
            w.blit(value, (position[0]*50 +15, position[1]*50))
            pygame.display.update()
            return

        else: # means that user has clicked on answers through (s)olve
            
            pygame.draw.rect(w,bgc , (position[0]*50 + buff, position[1]*50 + buff, 50 - 2* buff, 50 - 2* buff)) # redraw the square
            value = myfont.render(str(board1[i-1][j-1]), True, (0,0,0) ) # put that number back in the box
            w.blit(value, (position[0]*50 +15, position[1]*50))
            pygame.display.update()
            return
           
                

# dealing with user clicking on an empty box

        
    while True:

        
        for event in pygame.event.get(): # event after a click could be a key pressed or a quit.
            
            
            if event.type == pygame.QUIT:
                want_to_quit = True 
                return

            elif event.type ==  pygame.KEYDOWN: 
                if( board1[i-1][j-1]!= "." ): # dont want user to change the skeleton (safety)
                    return

                elif(event.key == 115 or event.key == 83): # if user hits solve
                    solveSudoku(board1, w)
                    is_solved[board_tracker//3] = True
                    text = myfont.render("Hope you enjoyed playing!", False, (0,191,255))
                    pygame.draw.rect(w, bgc, (25, 840, 1000, 500 ))
                    w.blit(text, (25, 840))
                    pygame.display.update() # display the board
   
                elif(event.key == 67 or event.key == 99): # User types 'c' or 'C'

                    pygame.draw.rect(w,bgc , (position[0]*50+ buff, position[1]*50 + buff, 50- 2*buff, 50-2*buff )) # redraw the square
                    if(board2[i-1][j-1] != "."):
                        value = myfont.render(str(board2[i-1][j-1]), True, (0,0,0) ) # put that user inputted number back in the box
                        w.blit(value, (position[0]*50 +15, position[1]*50))
                        
                    pygame.display.update()
                    check_board(board2, w)

                elif(event.key == 48) : # if user wants to delete an entry and types 0 
                    board2[i-1][j-1] = "." 
                    pygame.draw.rect(w, bgc, (position[0]*50+ buff, position[1]*50 + buff, 50- 2*buff, 50-2*buff ))
                    pygame.display.update()


                elif(0< event.key-48 <10): # user gives valid input
                    
                    
                    pygame.draw.rect(w, bgc, (position[0]*50+ buff, position[1]*50 + buff, 50- 2*buff, 50-2*buff )) # makes us edit a square directly
                    value = myfont.render(str(event.key -48 ), True, (0,0,0))
                    w.blit(value, (position[0]*50 +15, position[1]*50))
                    board2[i-1][j-1] = event.key -48
                    pygame.display.update()
                    return
                    


               # simply invalid input by user (eg. user pressed on any non numerical input other than 'c', 's', 'C', 'S' )
        
                else:
                    pygame.draw.rect(w,bgc , (position[0]*50+ buff, position[1]*50 + buff, 50- 2*buff, 50-2*buff )) # redraw the square regardless if blank or filled
                    
                    if( board1[i-1][j-1]== "." ): # if user has clicked on an editable square

                        if(board2[i-1][j-1] != "."): # if the user had inputted a number on that square
                            value = myfont.render(str(board2[i-1][j-1]), True, (0,0,0) ) # put that user inputted number back in the box
                            w.blit(value, (position[0]*50 +15, position[1]*50))
                        
                    pygame.display.update()


                return

        
    


def solveSudoku( board, w): # backtrack Algorithm
    
        global myfont

        def find_empty(board):

            for a in range(9):
                for b in range(9):

                    if(board[a][b] == "."):
                        return a,b

            return None



        def solver(board): 
           
            
            if(find_empty(board) is None):
                return True

            else:
                i, j = find_empty(board)

                for k in range(1,10):
                    if is_valid(board, i , j , k):
                        board[i][j] = str(k)
                        pygame.draw.rect(w, bgc, ((j+1)*50+ buff, (i+1)*50 + buff, 50- 2*buff, 50-2*buff )) # makes us edit a square directly
                        value = myfont.render(str(k), True, (0,0,0) )
                        w.blit(value, ((j+1)*50 +15, (i+1)*50))
                        
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


    global myfont
    global myfont2 

    if(mytruth == False): # just for safety 
    
            for k in range(9): # check all column entries in the same row
                
                if(board[i][k] == "."):
                    continue
                
                if (int(board[i][k]) == num) and (j != k ):

                    # we must make sure that we retain the colors of the question and the user input number

                    pygame.draw.rect(w, (220,20,60), ((j+1)*50, (i+1)*50, 50, 50)) # draw a red square at (i, j)
                    
                    value1 = myfont.render(str(num), True, (0,0,0)) # black again because (i,j) is a user entry 
                        
                    w.blit(value1, ((j+1)*50 +15, (i+1)*50))
                    

                    pygame.draw.rect(w, (220,20,60), ((k+1)*50, (i+1)*50, 50, 50 )) # draw a red square at i, k


                    if(board1[i][k] == "."): # [i][k] is not an original position that has a number
                        value2 = myfont.render(str(num), True, (0,0,0))

                    else: # there is a number on the original board
                        if(int(board1[i][k]) == num ): 
                            value2 = myfont.render(str(num), True, col_q)
                        
                    w.blit(value2, ((k+1)*50 +15, (i+1)*50)) 

                    pygame.display.update()

                    time.sleep(2)

                    # we must redraw the normal squares back

                    pygame.draw.rect(w, bgc, ((j+1)*50, (i+1)*50, 50, 50 )) # draw the normal square again at i, j
                    w.blit(value1, ((j+1)*50 +15, (i+1)*50))
                    pygame.draw.rect(w, bgc, ((k+1)*50, (i+1)*50, 50, 50)) # draw a normal square again at i, k
                    w.blit(value2, ((k+1)*50 +15, (i+1)*50))

                    draw_board(w)
                    pygame.display.update()

                    return False

            for k in range(9): # check column

                if(board[k][j] == ".") : # if empty slot we continue because it does not contradict with anything
                    continue
                
                if (int(board[k][j]) == num) and (i != k ):

                    pygame.draw.rect(w, (220,20,60), ((j+1)*50, (i+1)*50, 50, 50)) # draw a red square at i, j
                    value1 = myfont.render(str(num), True, (0,0,0))          
                    w.blit(value1, ((j+1)*50 +15, (i+1)*50))

                    pygame.draw.rect(w, (220,20,60), ((j+1)*50, (k+1)*50, 50, 50)) # draw a red square at k, j

                    if(board1[k][j] == "."): #  [k][j] is not an original position that has a number
                        value2 = myfont.render(str(num), True, (0,0,0))

                    else: # there is a number on original board
                        if(int(board1[k][j]) == num ): 
                            value2 = myfont.render(str(num), True, col_q)
                        
                    w.blit(value2, ((j+1)*50 +15, (k+1)*50))

                    pygame.display.update()

                    time.sleep(2)
                    
                     # we must redraw the normal squares back

                    pygame.draw.rect(w, bgc, ((j+1)*50, (i+1)*50, 50, 50 )) # draw the normal square again at i, j
                    w.blit(value1, ((j+1)*50 +15, (i+1)*50))
                    
                    pygame.draw.rect(w, bgc, ((j+1)*50, (k+1)*50, 50, 50 )) # draw a normal square again at k, j
                    w.blit(value2, ((j+1)*50 +15, (k+1)*50))
                    
                    draw_board(w)
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
                         

                         pygame.draw.rect(w, (220,20,60), ((j+1)*50, (i+1)*50, 50, 50 )) # draw a red square at i, j

                         value1 = myfont.render(str(num), True, (0,0,0))
                         w.blit(value1, ((j+1)*50 +15, (i+1)*50))

                         pygame.draw.rect(w, (220,20,60), ((n+1)*50, (m+1)*50, 50, 50 )) # draw a red square at m, n

                         if(board1[m][n] == "."): #  [m][n] is not an original position that has a number
                             value2 = myfont.render(str(num), True, (0,0,0))

                         else: # there is a number on original board

                             if(int(board1[m][n]) == num ): 

                                 value2 = myfont.render(str(num), True, col_q)
                        

                         w.blit(value2, ((n+1)*50 +15, (m+1)*50))

                         pygame.display.update()

                         time.sleep(2)
                    
                     # we must redraw the normal squares back

                         pygame.draw.rect(w, bgc, ((j+1)*50, (i+1)*50 , 50, 50)) # draw the normal square again at i, j
                         w.blit(value1, ((j+1)*50 +15, (i+1)*50))
                        
                         pygame.draw.rect(w, bgc, ((n+1)*50, (m+1)*50, 50, 50)) # draw a normal square again at m, n
                         w.blit(value2, ((n+1)*50 +15, (m+1)*50))

                         draw_board(w)

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


def check_board(board, w): ## tells you if your board is in a solved state  (always calling on board2)

    global myfont 
    global myfont2 
    
    for i in range(9):
        for j in range(9):

            if(board1[i][j] != "."): # if the initial board has a number on [i][j]
                continue # don't need to check if our original number is valid
                
            
            # i, j has to be a user entry at this point
            # dealing with blank squares or user inputs

            if(board[i][j] != "."): # if user has inputted a number here, we want to check is that is valid.
                if not is_valid_d(w, board, i, j, int(board[i][j]), False): ## if there is a position that is not valid in user's attempt. 

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

                pygame.draw.rect(w, (220,20,60), ((j+1)*50, (i+1)*50, 50, 50)) # draw a red square at the first empty cell
                pygame.display.update() # display the board
                time.sleep(1.5)
                pygame.draw.rect(w, bgc, ((j+1)*50, (i+1)*50, 50, 50)) # draw back a white square
                draw_board(w)
                pygame.display.update() # display the board    
                return


 # we have validated each non empty cell already. We also know there is no empty cell left. Thus the user has solved the board. 
        
    text = myfont.render("Feedback: YOU WIN!! Go treat yourself!! You earned it!", False, (0,255,0))
    pygame.draw.rect(w, bgc, (25, 840, 1000, 500 ))
    w.blit(text, (25, 840))

    pygame.display.update() 
                            
    return


                                
def main():

    global board1
    global board2
    global board_3
    global break_out
    global is_solved
    global pos_x_forthewin
    global pos_y_forthewin
    global want_to_quit 

    
    
    while True:
        clock.tick(60)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1: # if there is left click
                pos = pygame.mouse.get_pos() # get coordinates of that click

                if(pos[0]<50 or pos[0]>500 or pos[1]<50 or pos[1]>500 ): # if user clicks outside the grid we just check if they clicked on try another

                    if(pos[0]<810 or pos[0]>966 or pos[1]<760 or pos[1]>800): # the user did not click on anything with functionality
                        continue

                    else: # 'try another' has been clicked
                        
                        set_another_board(w)
                        continue
                                        
                pos_x_forthewin = pos[0]//50
                pos_y_forthewin = pos[1]//50
                if(pos_x_forthewin > 9 or pos_y_forthewin > 9 or pos_x_forthewin < 0 or pos_y_forthewin < 0):
                    continue
                
                user(w, (pos_x_forthewin, pos_y_forthewin))# call to user function only when there is a click on the board

                if(want_to_quit): # user could have wantred to quit after selecting a box to fill
                    pygame.quit()
                    return

            
            if event.type ==  pygame.KEYDOWN: ## if there was a direct key pressed w/o a click

                if(event.key == 67 or event.key == 99): # if that key is for check
                    if(is_solved[board_tracker//3] != True):
                        check_board(board2, w) # want to check the user's board

                if(event.key == 115 or event.key == 83): # if that key was for solve
                    solveSudoku(board1, w)
                    is_solved[board_tracker//3] = True
                    text = myfont.render("Hope you enjoyed playing!! Have a lovely day :)", False, (0,191,255))
                    pygame.draw.rect(w, bgc, (25, 840, 1000, 500 ))
                    w.blit(text, (25, 840))
                    pygame.display.update() # display the board






def set_another_board(w): # this function will draw a new board and input numbers into it and make sure the back end has been adjusted as well.

    global board1
    global board2
    global board3
    global break_out
    global board_tracker
    global is_solved
    
    board_tracker += 3 
    
    if(board_tracker >9):
        board_tracker = 0
        
    board1 = allboards[board_tracker]
    board2 = allboards[board_tracker+1]
    board3 = allboards[board_tracker+2]

    w.fill((255,255,255), (50, 50, 450, 450))
    draw_board(w) # want to check the user's board
    pygame.display.update() # display the board

    if(is_solved[board_tracker//3] == False):
        
        for i in range(9):
            for j in range(9): ## put in values to our board

                if(board1[i][j]!= "."):
                    val = myfont.render(board1[i][j], True, col_q)  
                    w.blit(val, ((j+1)*50 +15, (i+1)*50  ))

                elif(board2[i][j]!= "."):  # Board 1 position is blank here. But board2 position is filled by user, display it
                    val = myfont.render(str(board2[i][j]), True, (0,0,0)) # val is a surface that we will blit onto window w  
                    w.blit(val, ((j+1)*50 +15, (i+1)*50  ))

                        
                else:
                    continue

    else: 
        
        for i in range(9):
            for j in range(9): ## put in values to our board
                
                if(board3[i][j]!= "."):
                    val = myfont.render(board1[i][j], True, col_q) # val is a surface that we will blit onto window w  
                    w.blit(val, ((j+1)*50 +15, (i+1)*50  ))

                else: # use board 1 to fill in the solved stuff.
                        
                    val = myfont.render(board1[i][j], True, (0,0,0)) # val is a surface that we will blit onto window w  
                    w.blit(val, ((j+1)*50 +15, (i+1)*50  )) 
            
    
    
    pygame.draw.rect(w, bgc, (25, 840, 1000, 500 ))
    pygame.display.update()


main() # call main() function

# End of Program. 



