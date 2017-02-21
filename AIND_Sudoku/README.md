# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: The definition of naked twins is two different boxes in the same unit, which contain two same potential values. So we could eliminate the probability of these two potential values existing in other boxes within the same unit after we found naked twins in one unit.

In my implementation, I filter all boxes that with only two potential values. Then, get the naked twins among these which contain same element. We could eliminate potential values(naked twins values) from all the box in the same unit contains naked twins, beside naked twins boxes.

In the reduce puzzle function, we add `naked_twins` between `eliminate` and `only_choice` functions to reduce the probability for all boxes first, then get the `only_choice` value probability will increase compared with non-naked twins constraint propagation.

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: Adding diagonal constraints, like horizontal, vertical and square constraints. There are two diagonal units in diagonal constraints, one is `[s+t for s,t in zip(rows, cols)]`, and the other is `[s+t for s,t in zip(rows, cols[::-1])]`.

### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project.
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solutions.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the ```assign_values``` function provided in solution.py

### Data

The data consists of a text file of diagonal sudokus for you to solve.
