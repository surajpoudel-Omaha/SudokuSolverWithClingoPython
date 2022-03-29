# Suraj Poudel 
# CSCI 4220
# Surajpoudel@unomaha.edu
# Jorge Fandinno
import sys, clingo
from typing import List
from clingo import Model
answer_file_name = 'answer.txt'
class Context:

    def __init__(self):
        self.__sudoku = []
         
    def load(self, files):
        if len(files) != 1:
            sys.stderr.write("Invalid input format: a single input file must be provided\n")
            return False
        for f in files:
            if not self._load(f):
                return False
        return True

    def _load(self, file):
        f = open(file, 'r')
        lines = f.readlines()
        y = 0
        for line in lines: 
            y += 1
            if len(line) == 1:
                y -= 1
            x = 0
            values = line.strip().split()                  
            for value in values:
                vals = value.strip()
                x += 1
                if vals != "-" :
                    xAxis = clingo.Number(x)
                    yAxis = clingo.Number(y)
                    val = clingo.Number(int(vals))
                    sudokus = clingo.Tuple_((xAxis,yAxis,val))
                    self.__sudoku.append(sudokus) 
                else:
                    continue     
        return True

    def sudoku(self) -> List[clingo.Symbol]:
        return self.__sudoku

class ClingoApp(clingo.application.Application):
      
    def print_model(self, model, printer):
        clingoSymboolsToGrid = [[0]*9 for sudoku in range(9)]      
        for symbol in model.symbols(atoms=True):
            if symbol.name == 'sudoku':
                clingoSymboolsToGrid[int(str(symbol.arguments[1])) - 1][ int(str(symbol.arguments[0])) - 1] = int(str(symbol.arguments[2]))
        columncount = 0 
        rowCount = 0
        for row in clingoSymboolsToGrid:
            rowCount += 1
            for columnValue in row:
                print(columnValue, end = " ")
                columncount += 1
                if columncount % 3 == 0:
                    print("\t", end="")     
                if columncount / 3 == 0:
                    print()  
            if rowCount % 3 == 0:
                    print()     
            print()
    
    def main(self, ctl, files): 
        ctl.load("sudoku.lp")
        ctl.load("sudoku_py.lp")
        context = Context()
        if context.load(files):
            ctl.ground([("base", [])], context)
            ctl.solve()            
clingo.application.clingo_main(ClingoApp())


    
