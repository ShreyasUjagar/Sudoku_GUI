# Sudoku GUI (Graphic Interface Model) by Shreyas Ujagar

This is a Sudoku game implemented with Python. In order to play it you need to have pygame installed on your system (as this project uses the Pygame library) 

It consists of several features such as an instant time solver, a checker that provides clear feedback, and a handful of additional puzzles.

The solver implements a recursive backtracking algorithm that works as follows.
It inserts a valid number on the first empty slot, then goes to the next empty slot and does the same (until the puzzle has been solved).
If it reaches a slot where every number from 1-9 is invalid, then it 'backtracks' and returns to the previous slot.
The solver then inputs the next valid number into that previous slot and we continue moving forward.

Please note that the solutions for the puzzles are **not hardcoded** into the game and the solver gets to an answer each and every time.

I hope you enjoy this project as much as I enjoyed making it :)



I have used the following youtube videos that have helped me understand this algorithm and the Pygame tool which are cited below.

https://www.youtube.com/watch?v=eqUwSA0xI-s&t=5s

https://www.youtube.com/watch?v=lK4N8E6uNr4&t=37s

https://www.youtube.com/watch?v=_Z9Mz2V-Mig

https://www.youtube.com/watch?v=I2lOwRiGNy4                  (I have implemented my sudoku grid and formatted it based on this tutorial)

https://www.youtube.com/watch?v=IyHb_g2kHDQ


