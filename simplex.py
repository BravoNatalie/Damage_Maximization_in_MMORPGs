
import numpy
from gurobipy import *
import csv


infile = open("data.txt",'r')

reader = csv.reader(open("spells.csv","rb"),delimiter=";")
l = list(reader)
spells = numpy.array(l).astype("float")


lines = infile.readlines()
n_spells = int(lines[0])
MRR = int(lines[1])
TF = int(lines[2])
TT = int(lines[3])

infile.close()
var = []



try:
    # Create a new model
    m = Model("games")

    # Create variables
    for x in range(0,n_spells):
        var.append(m.addVar(vtype=GRB.INTEGER, name="x" + str(x)))

    # Set objective
    expr = LinExpr()
    for x in range(0,n_spells):
        expr += var[x]*spells[x][1]/TT  #Define somatorio onde spells[x][1] = Dmgx
    m.setObjective(expr,GRB.MAXIMIZE)   

    # Add constraint: x + 2 y + 3 z <= 4
    m.addConstr(x + 2 * y + 3 * z <= 4, "c0")

    # Add constraint: x + y >= 1
    m.addConstr(x + y >= 1, "c1")

    m.optimize()

    for v in m.getVars():
        print('%s %g' % (v.varName, v.x))

    print('Obj: %g' % m.objVal)

except GurobiError as e:
    print('Error code ' + str(e.errno) + ": " + str(e))

except AttributeError:
    print('Encountered an attribute error')
