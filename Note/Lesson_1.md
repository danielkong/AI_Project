Project 1 -- Sudoku AI

* Two Fundational AI tech
    - Constraint Propgation
        + elimination,
        + only_choice
        such as: map coloring, Crypto-Arithmetic Puzzles
    - search -- if constraint Propgation could not work.  
        + DFS search
        + extension: Naked Twins, Diagonal Sudoku


Project 2 -- Game-Playing

* Two AU strategies
    - Minimax
    - Alpha-beta pruning

Lab Pac-Man

* search tech
    - BFS
    - DFS
    - A-star Search

Project 3 Sign Language

* Hidden Markov Models

Term 2

* Recurrent neural network with Amazon Alexa Team
* Deep learing based system with IBM watson
* Convolutional Neural Network with MIT Affectiva

#Lesson 2#

Setting up with Anaconda
    conda create -n tea-facts python=3
    source activate tea-facts
    conda install numpy pandas matplotlib
    conda install jupyter notebook
    conda list

Anaconda

    * managing packages
    * environments
        conda create -n env_name list of packages
    * saving and loading environments
        save: conda env export > environment.yaml
        create a env from env file: conda env create -f env_file_name.yaml
        conda env list
        conda env remove -n env_name

Python Version - 3
    main breakage between 2 and 3
        print "Hello" // 2
        print("Hello") // 3

Create conda env for AI ND
