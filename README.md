# Sudoku GUI (Graphic Interface Model) by Shreyas Ujagar

This is a Sudoku game implemented with the Python language and the Pygame Library. In order to play, you would need to have both installed on your system.

It consists of several features such as an instant time solver, a checker that provides clear feedback, and a handful of additional puzzles.

The solver implements a recursive backtracking algorithm that works as follows.
It inserts a valid number on the first empty slot, then goes to the next empty slot and does the same (until the puzzle has been solved).
If it reaches a slot where every number from 1-9 is invalid, then it 'backtracks' and returns to the previous slot.
The solver then inputs the next valid number into that previous slot and we continue moving forward.

Please note that the solutions for the puzzles are **not hardcoded** into the game and the solver gets to an answer each and every time.

I hope you enjoy playing this as much as I enjoyed making it :)



https://github.com/ShreyasUjagar/Sudoku_GUI/assets/135226247/19484d3a-da24-4699-97f5-a6fef6a9f5c1



