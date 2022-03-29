% Please insert the names and email addresses of the group members:
% Suraj Poudel 
% surajpoudel@unomaha.edu
% CSCI 4220

{sudoku(X,Y,N) : possibleValueForACell(N)} = 1 :- position (X,Y).
% achieved: all the possible combination for sudoku.

cell(X,Y,(((X-1)/subgrid_size)*subgrid_size + (Y-1)/subgrid_size),N) :- sudoku(X,Y,N).
% achieved: each cell is assigned to a sub grid.

:- sudoku(X,Y,N), sudoku(A,Y,N), X!=A.
% achieved: removed all the cell where the sudoku had repeting number in a Row.

:- sudoku(X,Y,N), sudoku(X,B,N), Y!=B.
% achieved: removed the cell where the sudoku had repeting number in a Column.

:- cell(X,Y,S,N), cell(A,B,S,N), X!=A,  Y!=B. 
% achieved: Check if multiple cell is in the same sub grid and has the same Number.

#show sudoku/3.
