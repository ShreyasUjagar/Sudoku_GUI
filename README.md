# Sudoku GUI (Graphic Interface Model) by Shreyas Ujagar

This is a Sudoku game implemented with the Python language and the Pygame Library. In order to play, you would need to have both installed on your system. You can download
[Python](https://www.python.org/downloads/) and [Pygame](https://pypi.org/project/pygame/) here on their official websites.

It consists of several features including a robust instant time solver, a razor-sharp checker that validates any user input, and an abundance of additional puzzles.

## The Solver's Recursive Backtracking Algorithm

Starting at the top-most row, moving from left to right, the solver seeks the first empty slot.
Once that empty slot is found, it starts checking for a valid digit it can pencil in (a valid digit is one that does not conflict with any other entry within the same row, column and 3x3 square). So the solver busily begins iterating from 1 to 9, and enters the first number that is valid. Now a 'recursive call' is made to the solver method and the quest for the next empty slot begins. This process continues until the solver moves down to the last row and the puzzle has been solved.
**However**, if the solver reaches an empty slot where every number from 1-9 is invalid, it 'backtracks' and returns to the previous slot it edited.
Here, the next valid number is entered (into that previous slot) and we continue moving forward. This way, the solver effeciently gets to a solution in real time.

But how does it know if a number is valid or not at a certain position? The solver gets this information by calling an 'is_valid' method that takes as parameters the digit at the slot, and the position of that slot (row,col) and linearly checks if there are any number conflicts. The method will then accordingly return the boolean value 'True' or 'False' back to the solver.

Please note that the solutions for the puzzles are **not hardcoded** into the game and the solver gets to an answer each and every time.

I hope that my project will spark joy and challenge for you, much as the process of creating it did for me.



https://github.com/ShreyasUjagar/Sudoku_GUI/assets/135226247/19484d3a-da24-4699-97f5-a6fef6a9f5c1



