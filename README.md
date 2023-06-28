# Sudoku GUI (Graphic Interface Model) by Shreyas Ujagar

This is a Sudoku game implemented with the Python language and the Pygame Library. In order to play, you would need to have both installed on your system. You can download
[Python](https://www.python.org/downloads/) and [Pygame](https://pypi.org/project/pygame/) here on their official websites.

It consists of several features including a robust instant time solver, a razor-sharp checker that validates any user input, and an abundance of additional puzzles.

The solver implements a **recursive backtracking** algorithm that works as follows.
This solver scans over all the Sudoku slots going left to right on each row, starting at the top most row.
At the first empty slot it finds, it inserts the first valid number (starting from 1 to 9), then goes to the next empty slot and does the same (...until the puzzle has been solved).
If it reaches a slot where every number from 1-9 is invalid, then it 'backtracks' and returns to the previous slot.
The solver then inputs the next valid number into that previous slot and we continue moving forward. This way, the solver will effeciently get to a solution in real time.

How does it know if a number is valid or not at a certain position? The solver gets this information by calling an 'is_valid' method that takes as parameters the digit at the slot, and the position of that slot (row,col) and linearly checks if there are any number conflicts. The method will then accordingly return either the boolean value 'True' or 'False' back to the solver.

Please note that the solutions for the puzzles are **not hardcoded** into the game and the solver gets to an answer each and every time.

I hope you enjoy playing this as much as I enjoyed making it :)



https://github.com/ShreyasUjagar/Sudoku_GUI/assets/135226247/19484d3a-da24-4699-97f5-a6fef6a9f5c1



