% Suraj Poudel 
% surajpoudel@unomaha.edu
% CSCI 4220

#const subgrid_size=3.
% Achieved : created a constant to have subgrid size.

possibleValueForACell(1..subgrid_size*subgrid_size).
% achieved: A fact to give a cell a number.

position(1..subgrid_size*subgrid_size, 1..subgrid_size*subgrid_size).
% achieved: created a complete Grid using the subgrid size.

sudoku(X,Y,N):- (X,Y,N) = @sudoku().
% achieved: a link between the sudoku.py