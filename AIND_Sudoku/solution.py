assignments = []

def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [s+t for s in A for t in B]

rows = 'ABCDEFGHI'
cols = '123456789'

## List of all the boxes
boxes = cross(rows, cols)

## Units for Horizontal Contraints
row_units = [cross(r, cols) for r in rows]

## Units for Vertical Contraints
column_units = [cross(rows, c) for c in cols]

## Units for Square Contraints
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]

## Units for Diagonal Constraints
diag_units =  [[s+t for s,t in zip(rows, cols)],[s+t for s,t in zip(rows, cols[::-1])]]

## List of all the units
unitlist = row_units + column_units + square_units + diag_units

## Dict for all the boxes and corresponding list of units
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)

## Dict for all the peers for given box
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)

def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """
    # Find all instances of naked twins
    possible_twins = []
    for unit in unitlist:
        possible_twins += [((u, v), unit) for u in unit for v in unit if u != v and len(values[u]) == 2 and values[u] == values[v]]

    possible_naked_twins = {}
    for twins, unit in possible_twins:
        if twins not in possible_naked_twins.keys():
            possible_naked_twins[twins] = []
        possible_naked_twins[twins] += [unit]

    naked_twins = {}
    for possible_naked_twin_key, possible_naked_twin_value in possible_naked_twins.items():
        if len(possible_naked_twins) > 1:
            naked_twins[possible_naked_twin_key] = possible_naked_twin_value

    # Eliminate the naked twins as possibilities for their peers in same unit
    for naked_twin_key, naked_twin_value in naked_twins.items():
        for unit in naked_twin_value:
            for box in unit:
                if box not in naked_twin_key:
                    for value in values[naked_twin_key[0]]:
                        values = assign_value(values, box, values[box].replace(value,''))
    return values

def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    chars = []
    digits = '123456789'
    for ch in grid:
        if ch in digits:
            chars.append(ch)
        if ch == '.':
            chars.append(digits)
    assert len(chars) == 81, "Input grid must be a string of length 81 (9x9)"
    return dict(zip(boxes, chars))

def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    width = 1 + max(len(values[s]) for s in boxes)
    line = '+'.join(['-' * (width * 3)] * 3)
    for r in rows:
        print(''.join(values[r + c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    print

def eliminate(values):
    # Write a function that will take as an input, the sudoku in dictionary form,
    # run through all the boxes, applying the eliminate technique,
    # and return the resulting sudoku in dictionary form.
    #print(values)
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    for solved_val in solved_values:
        digit = values[solved_val]
        for peer in peers[solved_val]:
            values = assign_value(values, peer, values[peer].replace(digit,''))
    return values

def only_choice(values):
    """Finalize all values that are the only choice for a unit.

    Go through all the units, and whenever there is a unit with a value
    that only fits in one box, assign the value to this box.

    Input: Sudoku in dictionary form.
    Output: Resulting Sudoku in dictionary form after filling in only choices.
    """
    for unit in unitlist:
        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
                values = assign_value(values, dplaces[0], digit)
    return values

def reduce_puzzle(values):
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])

        values = eliminate(values)
        values = naked_twins(values)
        values = only_choice(values)

        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        stalled = solved_values_before == solved_values_after
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values

def search(values):
    "Using depth-first search and propagation, create a search tree and solve the sudoku."
    # First, reduce the puzzle using the previous function
    values = reduce_puzzle(values)

    if values is False:
        return False

    if all(len(values[s]) == 1 for s in boxes):
        return values

    # Choose one of the unfilled squares with the fewest possibilities
    n,s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
    # Now use recurrence to solve each one of the resulting sudokus, and
    for value in values[s]:
        new_sudoku = values.copy()
        new_sudoku = assign_value(new_sudoku, s, value)
        attempt = search(new_sudoku)
        if attempt:
            return attempt

def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    return search(grid_values(grid))

if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
